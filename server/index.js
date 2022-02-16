const http = require("http");
const socket = require("socket.io");
const express = require("express");
const app = express();
const server = http.createServer(app);
const fs = require('fs');

const io = socket(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"],
  },
});

const data_dict = {}

setInterval(() => {
  for (const uid of Object.keys(data_dict)) {
    const difference = new Date().getTime() - data_dict[uid].last_updated.getTime()
    var secondsDifference = Math.floor(difference / 1000);
    if (secondsDifference > 10) {
      const data_to_save = { ...data_dict[uid], last_updated: data_dict[uid].last_updated.getTime() }
      fs.writeFile(`./data/${uid}_${data_dict[uid].snapshotId}.json`, JSON.stringify(data_to_save), (err) => {
        if (err) throw err;
      });
    }
  }
}, 1000)

const save_data = (uid) => {
  return new Promise((resolve, reject) => {
    if (data_dict[uid] !== undefined && data_dict[uid].data.length > 0) {
      console.log("Saving data")
      fs.writeFile(`./data/${uid}_${snapshotId}.json`, data_dict[uid], (err) => {
        if (err) reject(err);
        resolve()
      });
    } else {
      resolve()
    }
  })
}

const reset_data = (uid) => {
  data_dict[uid] = { uid: uid, snapshotId: snapshotId, data: [], last_updated: new Date() }
}

io.use(async (socket, next) => {
  const uid = socket.handshake.auth.uid;
  socket.uid = uid
  next()
});

io.on("connection", (socket) => {

  console.log("Client connected: " + socket.uid);

  socket.on("sendImage", async ({ uid, snapshotId, image }) => {
    console.log("Snapshot from ", uid)
    var base64Data = image.replace(/^data:image\/png;base64,/, "");
    fs.writeFile(`./data/${uid}_${snapshotId}.png`, base64Data, 'base64', function (err) {
      console.log(err);
    });
    await save_data(uid);
    reset_data(uid)

  });

  socket.on("sendMousePosition", async ({ uid, snapshotId, position }) => {
    console.log("position from " + uid + ": " + position.x + " " + position.y)
    if (data_dict[uid]) {
      const date = new Date()
      data_dict[uid].data.push({ x: position.x, y: position.y, timestamp: date.getTime() })
      data_dict[uid].last_updated = date
    }
  });

  socket.on("disconnect", (socket) => {
    console.log("Client disconnected: " + socket.uid);
    save_data(socket.uid)
    reset_data(socket.uid)
  });
});




server.listen(4001, () => console.log("Server Running"));