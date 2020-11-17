//#region 是不是手機
function detectMob() {
    return ( ( window.innerWidth <= 992 ) || ( window.innerHeight <= 600 ) );
  }
//#endregion

function GetPercentageWidth(){
  let innerWidth = window.innerWidth;     //網頁寬度
  let ScreenWidth = window.screen.width;  //螢幕寬度
  // console.log("ScreenWidth :"+ScreenWidth);
  // console.log("innerWidth :"+innerWidth);
  var PercentageWidth = Math.round(innerWidth*100/ScreenWidth);
  // console.log("%數: "+ PercentageWidth);
  return PercentageWidth;
}

function isEmpty(str) {
  return (!str || 0 === str.length);
}

