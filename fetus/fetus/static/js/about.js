const body = document.querySelector('body');
const swiper = new Swiper(".mySwiper", {
	autoplay: {
		delay: 5000,
	},
	disableOnInteraction: false,
	pauseOnMouseEnter: true,
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
	},
	breakpoints: {
		1080: {
			slidesPerView: 1,
			spaceBetween: 10,
		},
		1280: {
			slidesPerView: 3,
			spaceBetween: 30,
		},
	},
});
function changeObj(){
    if(detectMob()){
        body.classList.remove('active');
        return;
    }
    if(GetPercentageWidth()<85){
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