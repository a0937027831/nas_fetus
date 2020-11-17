
const body = document.querySelector('body');

function changeObj(){
    if(detectMob())
      return;
    if(GetPercentageWidth()<80){
        if(!body.classList.contains('active')){
            body.classList.add('active');
        }
        return;
    }
    else{
        if(body.classList.contains('active')){
            body.classList.remove('active');
        }
    }
}
changeObj();
window.addEventListener('resize',changeObj,false);
