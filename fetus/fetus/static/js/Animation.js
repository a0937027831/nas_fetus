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
        t1.fromTo(AnimateBG,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5', ease:"open" })
        .fromTo(AnimateBG2,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5', ease:"open" },"-=2")
        .fromTo(svgAnimatebx,1.5,{width:'40vw',height:'30vw'},{width:'7.4vw',height:'7.4vw',opacity:'0',ease:"open"},'+=0.5')
        .fromTo(navbar,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=0.5')
        .fromTo(circlebx,1.5,{opacity:'0',width:'450px',height:'450px'},{opacity:'1',width:'450px',height:'450px',ease:"elastic.out(1, 0.3)"},'-=1')
        .fromTo(indicator,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=1.5')
        .fromTo(footer,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=2')
    }else{
      t1.fromTo(AnimateBG,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5',display:'none', ease:"open" })
        .fromTo(AnimateBG2,2,{height:'50%',opacity:'1'},{height:'0%',opacity:'0.5',display:'none', ease:"open" },"-=2")
        .fromTo(svgAnimatebx,1.5,{width:'70vw',height:'60vw'},{width:'7.4vw',height:'7.4vw',opacity:'0',ease:"open"},'+=0.5')
        .fromTo(navbar,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=0.5')
        .fromTo(circlebx,1.5,{opacity:'0',width:'80vw',height:'80vw'},{opacity:'1',width:'80vw',height:'80vw',ease:"elastic.out(1, 0.3)"},'-=1')
        .fromTo(indicator,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=1.5')
        .fromTo(footer,1.5,{opacity:'0'},{opacity:'1',ease:"open"},'-=2')
    }
}
//#endregion



var imageArray = ["/static/static/image/banner/logo1.png","/static/static/image/banner/logo2.png","/static/static/image/banner/logo3.png"];
const clip_circle = document.querySelector(".clip_circle");
let count = 0;
let run = true;
var bannerArray=[];

function Get(URL){
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      MakeBannerList(JSON.parse(request.responseText),'');
    }else{
      console.log('status :'+request.statusText);
    }
  };
  request.open('GET', URL ,true);
  request.send();
}

function MakeBannerList(requestjson){
  try {
    if(requestjson[0].image1 == '' || requestjson[0].image1 == null ){
      return;
    }
  } catch (error) {
    console.error(error);
    return;
  }

  imageArray.splice(0,imageArray.length);
  // console.log(imageArray);
  addlist(imageArray,requestjson[0].image1);
  addlist(imageArray,requestjson[0].image2);
  addlist(imageArray,requestjson[0].image3);
  addlist(imageArray,requestjson[0].image4);
  addlist(imageArray,requestjson[0].image5);
  // console.log(imageArray);
  resetCircleIndicator();
}

function addlist(array,str){
  if(!isEmpty(str)){
    array.push(str);
  }
}

function autoPlay(){
  if(!run)
    return;
  count++;
  if(count == imageArray.length){
     count = 0;
  }
  changeSide();
}

function changeSide(){
    updateCircleIndicator();
    addImage();
    slide();
    setTimeout(deletePreviousImage(),1000);
}

function indicateSlide(element){
  if(count == element.id){
    return;
  }
  count = element.id;
  run = false;
  setTimeout(()=>{run = true;}, 5000);
  changeSide();
}

function circleIndicator(){
  for( i=0; i<imageArray.length; i++){
    const div = document.createElement("div");
    div.setAttribute("onclick","indicateSlide(this)")
    div.id = i;
    if(i==0)
      div.className="active";
    indicator.appendChild(div);
  }
}

function resetCircleIndicator(){
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
}

function updateCircleIndicator(){
  if(imageArray.length == 1){
    return;
  }else{
    for(i= 0; i<indicator.children.length; i++){
      indicator.children[i].classList.remove('active');
    }
    indicator.children[count].classList.add('active');
  }
}

function addImage(){
  let nextImage = imageArray[count];
  let img = document.createElement('img');
  img.src = nextImage;
  img.style.opacity = '0';
  img.classList.add("banner");
  clip_circle.appendChild(img);
}

function slide(){
    let allImages = document.querySelectorAll(".banner");
    TweenMax.to(allImages[0],1,{opacity:"0",ease:"power1.out"});
    TweenMax.to(allImages[1],1,{opacity:"1",ease: "circ.in"});
}

function deletePreviousImage(){
  let allImages = document.querySelectorAll(".banner");
  let currentImage = allImages[0];
  currentImage.remove();
}

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


Get('https://fetus.i234.me/bannerJson');
circleIndicator();
OpenAnimation();
setTimeout(()=>{setInterval(autoPlay,5000);},5000);
setTimeout(()=>{RemoveStyle();},6000);






