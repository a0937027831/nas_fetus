const AnimateBG = document.querySelector('.animateBG');
const AnimateBG2 = document.querySelector('.animateBG2');
const svgAnimatebx = document.querySelector('.svgAnimatebx');
const navbar = document.querySelector('.navbar');
const circlebx = document.querySelector('.circlebx');
const indicator = document.querySelector('.indicator');
const footer = document.querySelector('.footer');
const t1 = gsap.timeline();

//#region 開頭動畫
function OpenAnimation(){
    CustomEase.create("open", "M0,0 C0,0 0.167,0 0.2,0 0.236,0 0.327,0.084 0.384,0.16 0.432,0.224 0.482,0.28 0.52,0.39 0.696,0.982 0.818,1.001 1,1 ");
    CustomEase.create("MainOpen", "M0,0 C0.128,0 0.386,0 0.438,0 0.5,0 0.525,1 0.746,1 0.874,1 0.752,1 1,1 ");
    CustomEase.create('Jump',"M0,0 C0.14,0 0.183,0.447 0.208,0.572 0.244,0.752 0.3,1.014 0.312,1.08 0.356,0.974 0.422,0.578 0.476,0.6 0.552,0.63 0.613,0.983 0.62,1 0.639,0.973 0.668,0.909 0.7,0.9 0.767,0.88 0.773,1.007 0.788,1 0.818,0.984 0.878,0.948 0.911,0.948 0.956,0.948 1,1 1,1 ")
    if(!detectMob()){
        t1.fromTo(svgAnimatebx,1.5,{width:'40vw',height:'30vw'},{width:'7.4vw',height:'7.4vw',opacity:'0',ease:"open"},'+=0.5')
        .fromTo(navbar,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=0.5')
        .fromTo(circlebx,1.5,{opacity:'0',width:'450px',height:'450px'},{opacity:'1',width:'450px',height:'450px',ease:"elastic.out(1, 0.3)"},'-=1')
        .fromTo(indicator,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=1.5')
        .fromTo(footer,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=2')
    }else{
      t1.fromTo(svgAnimatebx,1.5,{width:'70vw',height:'60vw'},{width:'7.4vw',height:'7.4vw',opacity:'0',ease:"open"},'+=0.5')
        .fromTo(navbar,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=0.5')
        .fromTo(circlebx,1.5,{opacity:'0',width:'80vw',height:'80vw'},{opacity:'1',width:'80vw',height:'80vw',ease:"elastic.out(1, 0.3)"},'-=1')
        .fromTo(indicator,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=1.5')
        .fromTo(footer,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=2')
    }
}
//#endregion

// fromTo(AnimateBG,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5', ease:"open" })
//         .fromTo(AnimateBG2,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5', ease:"open" },"-=2")
// .fromTo(AnimateBG,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5',display:'none', ease:"open" })
//         .fromTo(AnimateBG2,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5',display:'none', ease:"open" },"-=2")


var imageArray = ["../static/image/banner/logo1.png","../static/image/banner/logo2.png","../static/image/banner/logo3.png"];
const clip_circle = document.querySelector(".clip_circle");
var count =0;
let run = true;
var bannerArray=[];

// 開始倫播
function StartBannerPlay(){
  CircleIndicator();
  addImage(1);
  setTimeout(()=>{setInterval(autoPlay,5000);},5000);
}
// --------

// 播放更改count
function autoPlay(){
  if(!run)
    return;
  count++;
  if(count == imageArray.length){
     count = 0;
  }
  changeSide();
}
//

function Get(URL){
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      MakeBannerList(JSON.parse(request.responseText),'');
    }else{
      console.log('status num: '+status);
      if(this.status == '404'){
        // console.log('獲取url失敗 使用預設');
        console.log('status :'+request.statusText);
        StartBannerPlay();
      }
    }
  };
  request.open('GET', URL ,true);
  request.send();
}


// 把資料塞進去
function MakeBannerList(requestjson){
  try {
    if(requestjson.image1 == '' || requestjson.image1 == null ){
      // console.log('Banner沒資料 使用預設');
      StartBannerPlay();
      return;
    }
  } catch (e) {
    console.error('json error'+e);
    return;
  }
  // console.log('Banner 有資料 使用後台資料');
  imageArray.splice(0,imageArray.length);
  addlist(imageArray,requestjson.image1);
  addlist(imageArray,requestjson.image2);
  addlist(imageArray,requestjson.image3);
  addlist(imageArray,requestjson.image4);
  addlist(imageArray,requestjson.image5);
  StartBannerPlay();
}
// --------------------------------

function changeSide(){
  if(imageArray.length > 1){
    updateCircleIndicator();
    slide();
  }
}

function clickchangeSide(lastid){
  if(imageArray.length > 1){
    updateCircleIndicator();
    clickslide(lastid);
  }
}

function indicateSlide(element){
  if(count == element.id){
    return;
  }
  last = count;
  count = element.id;
  run = false;
  setTimeout(()=>{run = true;}, 5000);
  clickchangeSide(last);
}

// 製作下方選項圈圈
function CircleIndicator(){
  // console.log("indicator.children.length"+indicator.children.length);
  for(i= indicator.children.length; i<imageArray.length; i++){
    const div = document.createElement("div");
    div.setAttribute("onclick","indicateSlide(this)");
    div.id = i;
    indicator.appendChild(div);
  }
  for(i= indicator.children.length; i>imageArray.length; i--){
      console.log(i-1)
      indicator.children[i-1].remove();
  }
  indicator.children[0].className="active";
}

// 下面圈圈倫播轉動功能
function updateCircleIndicator(){
  for(i= 0; i<indicator.children.length; i++){
    indicator.children[i].classList.remove('active');
  }
  indicator.children[count].classList.add('active');
}

function addImage(opacity){
  for(i=0;i<imageArray.length; i++){
    let nextImage = imageArray[i];
    let img = document.createElement('img');
    img.src = nextImage;
    img.style.opacity = 0;
    img.classList.add("banner");
    clip_circle.appendChild(img);
  }
  clip_circle.children[0].style.opacity = 1;
}

function slide(){
    // console.log("使用沒函數的");
    for(i = 0; i<imageArray.length; i++){
      if(i != count){
        clip_circle.children[i].style.opacity=0;
      }
    }
    if(count-1 == -1){
      TweenMax.to(clip_circle.children[imageArray.length-1],1,{opacity:"0",ease:"power1.out"});
      TweenMax.to(clip_circle.children[count],1,{opacity:"1",ease: "circ.in"});
    }else{
      TweenMax.to(clip_circle.children[count-1],1,{opacity:"0",ease:"power1.out"});
      TweenMax.to(clip_circle.children[count],1,{opacity:"1",ease: "circ.in"});
    }
}

function clickslide(lastid){
    // console.log("使用有函數的");
    for(i = 0; i<imageArray.length; i++){
      if(i != lastid){
        clip_circle.children[i].style.opacity=0;
      }
    }
    TweenMax.to(clip_circle.children[lastid],1,{opacity:"0",ease:"power1.out"});
    TweenMax.to(clip_circle.children[count],1,{opacity:"1",ease: "circ.in"});
}

// function deletePreviousImage(){
//   let allImages = document.querySelectorAll(".banner");
//   let currentImage = allImages[0];
//   currentImage.remove();
// }

//#region 刪除style
let IsMoble = detectMob();
function AutoReMove(){
  let check = detectMob();
  if(IsMoble != check){
     check = IsMoble;
     document.querySelector('.circlebx').removeAttribute("style");
  }
}
function RemoveStyle(){
  document.querySelector('.circlebx').removeAttribute("style");
}
//#endregion

// 功能 陣列增加
function addlist(array,str){
  if(!isEmpty(str)){
    array.push(str);
  }
}

// (手機電腦)主頁背景
const bg = document.querySelector('.bg');
const bg_moble = document.querySelector('.bg-moble');

function changeObj(){
    if(detectMob()){
      bg.style.display="none";
      bg_moble.style.display="unset";
    }else{
      bg.style.display="unset";
      bg_moble.style.display="none";
    }
}
changeObj();
window.addEventListener('resize',changeObj,false);


Get('https://yuan-pei.com//bannerJson');
OpenAnimation();
setTimeout(() => { RemoveStyle(); }, 6000);






