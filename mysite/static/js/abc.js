'use strict';
/*alert('window inner size: ' + window.innerWidth + ' x ' + window.innerHeight);

alert('appName = ' + navigator.appName + '\n' +
      'appVersion = ' + navigator.appVersion + '\n' +
      'language = ' + navigator.language + '\n' +
      'platform = ' + navigator.platform + '\n' +
      'userAgent = ' + navigator.userAgent);
*/

//alert(document.cookie);

function callback() {
        console.log('Done');
}
console.log('before setTimeout()');
setTimeout(callback, 2000); // 1秒钟后调用callback函数
console.log('after setTimeout()');


//'use strict';
//
//var canvas = document.getElementById('test-shape-canvas');
//var ctx = canvas.getContext('2d');
//
//ctx.clearRect(0, 0, 200, 200);
//ctx.fillStyle = '#dddddd';
//ctx.fillRect(10, 10, 130, 130);
//
//var path=new Path2D();
//path.arc(75, 75, 50, 0, Math.PI*2, true);
//path.moveTo(110,75);
//path.arc(75, 75, 35, 0, Math.PI, false);
//path.moveTo(65, 65);
//path.arc(60, 65, 5, 0, Math.PI*2, true);
//path.moveTo(95, 65);
//path.arc(90, 65, 5, 0, Math.PI*2, true);
//ctx.strokeStyle = '#0000ff';
//ctx.stroke(path);

var div = $('#abc'); 
var divDom = div.get(0);
//alert(divDom)

//var a = $('#test-link');
//a.on('click', function () {
//        alert('Hello!');
//}); 

$(function () { $('#test-link').click(function () { alert('Hello!'); }); });

var input = $('#test-input');
input.change(function () {
        console.log('changed...');
}); 

var div = $('#test-show-hide');
div.hide('10000');
