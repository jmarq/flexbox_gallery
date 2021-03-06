    var PADDING = 5;
    var thumbnail_section = document.querySelector(".thumbnails");
    var thumbnails = document.querySelectorAll(".thumbnail");
    console.log(thumbnails);
    for( var i=0; i < thumbnails.length; i +=1){ 
      var thumb = thumbnails[i];
      console.log(thumb);
      thumb.addEventListener("click", handleThumbnailClick);
    }
    var modal = document.querySelector(".modal");
    modal.addEventListener("click",handleModalClick);


    function thumbnailToSource(thumbnailSource){
      return thumbnailSource.replace("/thumbs","").replace(".thumbnail","");
    }

    function resizeImg(img){
      var orig_width = img.getAttribute("data-orig-width");
      var orig_height = img.getAttribute("data-orig-height");
      var width_ratio = orig_width / (window.innerWidth-PADDING);
      var height_ratio = orig_height / (window.innerHeight-PADDING);
      var greater_ratio = Math.max(width_ratio, height_ratio);
      if(greater_ratio > 1){
         img.width = orig_width/greater_ratio;
         //height set automatically based on width, thanx browser	 
      }
    }

    function handleThumbnailClick(event){
      var whichSlide = this.getAttribute("data-slide");
      console.log("thumbnail clicked");
      var img_src = this.src;
      img_src = thumbnailToSource(img_src);
      var slideClass = ".slide"+whichSlide;
      var slide = document.querySelector(".modal "+slideClass);
      slide.classList.add("shown");
      var modal_img = slide.querySelector("img");
      if(!modal_img.src){
        modal_img.src = img_src;
      }
      modal_img.onload = function(){
	  this.setAttribute("data-orig-width",this.width);
	  this.setAttribute("data-orig-height",this.height);
	  resizeImg(this);
      };
      var modal = document.querySelector(".modal");
      modal.classList.remove("hidden");
      thumbnail_section.classList.add("hidden");
    }

function windowResize(){
	      console.log("resize");
	            var slide_images = document.querySelectorAll(".slide img[src]");
		          for( var i = 0; i < slide_images.length; i+=1){
				          resizeImg(slide_images[i]);
					        }
			      }
    window.onresize=windowResize;
        
        function handleModalClick(event){
		      this.classList.add("hidden");
		            thumbnail_section.classList.remove("hidden");
			          modal.querySelector(".shown").classList.remove("shown");
				      }

