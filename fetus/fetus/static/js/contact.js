const body = document.querySelector('body');

function changeObj(){
    if(detectMob()){
        body.classList.remove('active');
        return;
    }
    if(GetPercentageWidth()<70){
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

