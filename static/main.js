$(document).ready(function () {
  const up = document.querySelector("#up"); //select the button
  const down = document.querySelector("#down"); //select the button
  const left = document.querySelector("#left"); //select the button
  const right = document.querySelector("#right"); //select the button

  //namespace = '/test';
  const socket = io();

  socket.on("connect", function () {
    socket.emit("ConnectionCheck", "connected to the SocketServer...");
  });

  // start functions
  const forwards = () => {
    //console.log("Going Forwards");
    socket.emit("forwards", "Going forwards");
  };

  const backwards = () => {
    //console.log("Going Backwards");
    socket.emit("backwards", "Going backwards");
  };

  const lefts = () => {
    //console.log("Going Left");
    socket.emit("left", "Going Left");
  };

  const rights = () => {
    //console.log("Going Right");
    socket.emit("right", "Going Right");
  };

  const leftUp = () => {
    //console.log("Going Right");
    socket.emit("up-left", "Going up-left");
  };

  const rightUp = () => {
    //console.log("Going Right");
    socket.emit("up-right", "Going up-right");
  };

  const leftDown = () => {
    //console.log("Going Right");
    socket.emit("down-left", "Going down-left");
  };

  const rightDown = () => {
    //console.log("Going Right");
    socket.emit("down-right", "Going down-right");
  };

  //end function
  const stop = () => {
    //console.log("stop");
    socket.emit("stop", "Stopping");
  };

  [
    [up, forwards],
    [right, rights],
    [down, backwards],
    [left, lefts],
    [lup, leftUp],
    [rup, rightUp],
    [ldown, leftDown],
    [rdown, rightDown],
  ].forEach((arrowFn) => {
    arrowFn[0].addEventListener("pointerdown", arrowFn[1]);
    arrowFn[0].addEventListener("pointerup", stop);
  });
});
