import React, { useState, PropsWithChildren } from 'react';
import { HeatmapProviderCtx } from './Context';
import { useEffect } from 'react';
import io, { Socket } from 'socket.io-client';
import html2canvas from 'html2canvas';

export interface HeatmapProviderProps {
  server: string;
  uid?: string;
}

export interface MousePositon {
  x: number;
  y: number;
}

export const useMousePosition = () => {
  const [position, setPosition] = useState<MousePositon>({ x: 0, y: 0 });

  useEffect(() => {
    const setFromEvent = (e: MouseEvent) => setPosition({ x: e.clientX, y: e.clientY });
    window.addEventListener('mousemove', setFromEvent);

    return () => {
      window.removeEventListener('mousemove', setFromEvent);
    };
  }, []);

  return position;
};

export const HeatMapProvider = (props: PropsWithChildren<HeatmapProviderProps>) => {
  const { children, uid, server } = props;
  const position = useMousePosition();

  const [socket, setSocket] = useState<Socket | null>(null);
  const [image, setImage] = useState<string | null>(null);
  const [snapshotId, setSnapshotId] = useState<string | null>(null);

  const record = async (snapshotId: string) => {
    const element = document.querySelector('body') as HTMLElement;
    const canvas = await html2canvas(element);
    const dataURL = canvas.toDataURL();
    setSnapshotId(snapshotId);
    setImage(dataURL);
  };

  useEffect(() => {
    try {
      const s = io(server);
      setSocket(s);
    } catch (error) {
      console.log(error);
    }
  }, []);

  useEffect(() => {
    if (socket && snapshotId) {
      socket.emit('sendMousePosition', {
        uid: uid || 'default',
        snapshotId: snapshotId,
        position: position,
      });
    }
  }, [position]);

  useEffect(() => {
    if (image && socket && snapshotId) {
      socket.emit('sendImage', {
        uid: uid || 'default',
        snapshotId: snapshotId,
        image: image,
      });
    }
  }, [image, socket]);

  return (
    <HeatmapProviderCtx.Provider
      value={{
        position: position,
        record: record,
      }}
    >
      {children}
    </HeatmapProviderCtx.Provider>
  );
};

export default HeatMapProvider;
