var robot = require("robotjs");
const ioHook = require('iohook');
const settings = require('./config')
const { getCode } = require('./config/keys')
ioHook.on("keyup", event => {
     console.log('press ',String.fromCharCode(event.rawcode));
     for(let i in settings) {
          if (event.rawcode === getCode(i)) {
               console.log('bigo', i)
               const targetKeys = settings[i]
               console.log('开始输入', targetKeys)
               
               for(let j in targetKeys) {
                    console.log('开始输入', targetKeys[j])
                    console.time('1')
                    // robot.keyTap(targetKeys[j]);
                    robot.keyToggle(targetKeys[j], 'down')
                    robot.setKeyboardDelay(0)
                    robot.keyToggle(targetKeys[j], 'up')
                    console.timeEnd('1')
               }
          }
     }
     // {keychar: 'f', keycode: 19, rawcode: 15, type: 'keypress'}
});
ioHook.start();

// const hook = require('node-iohook')


// hook.on('keydown', function(msg){
//     console.log(msg);
// });


// hook.start();