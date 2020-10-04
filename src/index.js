var robot = require("robotjs");
const ioHook = require('iohook');
console.log(ioHook.checkerAPI)
ioHook.on("keydown", event => {
     console.log(event);
     // {keychar: 'f', keycode: 19, rawcode: 15, type: 'keypress'}
});
ioHook.start(true);