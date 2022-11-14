$(document).ready(function () {
  const up = document.querySelector("#up"); //select the button
  const down = document.querySelector("#down"); //select the button
  const left = document.querySelector("#left"); //select the button
  const right = document.querySelector("#right"); //select the button

  //namespace = '/test';
  const socket = io();

  socket.on("connect", function () {
    socket.emit("my_event", "connected to the SocketServer...");
  });

  // start functions
  const forwards = () => {
    //console.log("Going Forwards");
    socket.emit("custom-event1", "Going forwards");
  };

  const backwards = () => {
    //console.log("Going Backwards");
    socket.emit("custom-event2", "Going backwards");
  };

  const lefts = () => {
    //console.log("Going Left");
    socket.emit("custom-event3", "Going Left");
  };

  const rights = () => {
    //console.log("Going Right");
    socket.emit("custom-event4", "Going Right");
  };

  //end function
  const stop = () => {
    //console.log("Stop");
    socket.emit("custom-event5", "Stopping");
  };

  [
    [up, forwards],
    [right, rights],
    [down, backwards],
    [left, lefts],
  ].forEach((arrowFn) => {
    arrowFn[0].addEventListener("pointerdown", arrowFn[1]);
    arrowFn[0].addEventListener("pointerup", stop);
  });
});
