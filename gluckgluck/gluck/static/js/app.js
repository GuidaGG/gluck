(function($) {
    
    $(document).ready(function() {

        $('.section_image_texts').each(function( index ) {
           divs =  $(this).find('div')
            divs.each(function( index ) {
                if(index%2!=0){
                var previousW = $(this).prev().css('width');
                var currentW = $(this).parent().css('width');
                var newwidth = parseInt(currentW) - parseInt(previousW)-100;
                $(this).css('width', newwidth + 'px')
                 }
             });
            })


                            
            // Detect request animation frame
            var scroll = window.requestAnimationFrame ||
            // IE Fallback
            function(callback){ window.setTimeout(callback, 1000/60)};
            var elementsToShow = document.querySelectorAll('img'); 

            function loop() {

            Array.prototype.forEach.call(elementsToShow, function(element){
            if (isElementInViewport(element)) {
            //element.classList.add('is-visible');

            } else {
            //element.classList.remove('is-visible');
            //element.classList.add('not-visible');

            }
            });

            scroll(loop);
            }

            // Call the loop for the first time
            loop();

            // Helper function from: http://stackoverflow.com/a/7557433/274826
            function isElementInViewport(el) {
            // special bonus for those using jQuery
            if (typeof jQuery === "function" && el instanceof jQuery) {
            el = el[0];
            }
            var rect = el.getBoundingClientRect();
            return (
            (rect.top <= 0
            && rect.bottom >= 0)
            ||
            (rect.bottom >= (window.innerHeight-200 || document.documentElement.clientHeight-200) &&
            rect.top <= (window.innerHeight || document.documentElement.clientHeight))
            ||
            (rect.top >= 0 &&
            rect.bottom <= (window.innerHeight-200| document.documentElement.clientHeight-200))
            );
            }

            window.onscroll = function() {myFunction()};
            var first = true
            function myFunction() {
                
                var banner = document.getElementById('header-banner');
                var inicial = banner.getBoundingClientRect().height;
                console.log(inicial);
                console.log(document.documentElement.scrollTop)
                if(document.documentElement.scrollTop<=inicial&& first == true ){
                banner.style.top = -document.documentElement.scrollTop*1.4 + "px";
         
                }
               
                if(document.documentElement.scrollTop>inicial/2-10){
                banner.style.display = "none";
                document.getElementById('space').style.display = 'none';
                first =false;
                } 

                //banner.style.top = 
            }

        })
    
 
})(jQuery);

