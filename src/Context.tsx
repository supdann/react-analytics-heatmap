import { createContext } from 'react';
import { MousePositon } from './HeatMapProvider';

interface IHeatmapProviderCtxProps {
  position: MousePositon;
  record: (snapshotId: string) => void;
}

export const HeatmapProviderCtx = createContext({} as IHeatmapProviderCtxProps);
