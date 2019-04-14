jQuery(document).ready(function($){

    $color_list = [

        {color:'#000000',title:'Black'},

        {color:'#ffffff',title:'White'},

        {color:'#d54e21',title:'Red'},

        {color:'#78a300',title:'Green'},

        {color:'#0e76a8',title:'Blue'},

        {color:'#9cc2cb',title:'Teal'},

        {color:'#73716e',title:'Grey'},

        {color:'#ff7700',title:'Orange'},

        {color:'#ffcc00',title:'Yellow'},

        {color:'#ff66b5',title:'Pink'},

        {color:'#6a5a8c',title:'Purple'}
        
    ];
    
    $('.color-picker').wrap('<div class="color-picker-wrap"></div>');

     $('.color-picker-wrap').each(function(){

            var self = $(this);

            if(self.children('.color-picker').hasClass('cp-sm')){

                self.addClass('cp-sm');

            }else if(self.children('.color-picker').hasClass('cp-lg')){

                self.addClass('cp-lg');

            }

            self.append('<ul></ul><input type="color" style="display:none;" />');

            var $foundactive = false;

            for(var i = 0; i <  $color_list.length; i++){

            var $active = '';

            if(self.children(".color-picker").val()==$color_list[i].color){

                    $active = 'class="active"';

                    $foundactive = true;

                    if(self.children(".color-picker").hasClass('cp-show')){

                        self.children('small').remove();    

                        self.append('<small>Selected Color: <code>'+$color_list[i].color+'</code></small>');
                        
                    }
            }

                self.children('ul').append('<li '+ $active+' style="background-color:'+$color_list[i].color+'" title="'+ $color_list[i].title+'"></li>');
            }

            if(!$foundactive && self.children(".color-picker").val()!='' ){

                    self.children('ul').append('<li class="active" title="Custom Color '+self.children(".color-picker").val()+'" style="background-color:'+self.children(".color-picker").val()+'"></li>');
                    
                    if(self.children(".color-picker").hasClass('cp-show')){

                        self.children('small').remove();    

                        self.append('<small>Selected Color: <code>'+self.children(".color-picker").val()+'</code></small>');
                        
                    }

            }

            self.children('ul').append('<li class="add_new" title="Add New">+</li>');

     });

  $('.color-picker-wrap ul').on('click','li', function() {

        var self = $(this);

          if (!self.hasClass('add_new')) {   

                  if (!self.hasClass('active')) {

                      self.siblings().removeClass('active');

                        var color =rgb2hex(self.css("backgroundColor"));

                        self.parents('.color-picker-wrap').children(".color-picker").val(color);

                        self.addClass('active');
                        
                        if(self.parents('.color-picker-wrap').children(".color-picker").hasClass('cp-show')){

                            self.parents('.color-picker-wrap').children('small').remove();    

                            self.parents('.color-picker-wrap').append('<small>Selected Color: <code>'+color+'</code></small>');

                        }

                  }
          }else{
              self.parents('.color-picker-wrap').children("input[type='color']").trigger('click');
          }

      });

  $(".color-picker-wrap input[type='color']").on("change",function(){

      var self = $(this);

      self.parents('.color-picker-wrap').children('ul').children('li').removeClass('active');

      self.parents('.color-picker-wrap').children('ul').children('li.add_new').remove();

      self.parents('.color-picker-wrap').children('ul').append('<li class="active" title="Custom Color '+self.val()+'" style="background-color:'+self.val()+'"></li>');

      self.parents('.color-picker-wrap').children(".color-picker").val(self.val());

      self.parents('.color-picker-wrap').children('ul').append('<li class="add_new" title="Add New">+</li>');
                              
    if(self.parents('.color-picker-wrap').children(".color-picker").hasClass('cp-show')){

        self.parents('.color-picker-wrap').children('small').remove();    

        self.parents('.color-picker-wrap').append('<small>Selected Color: <code>'+self.val()+'</code></small>');
        
    }

  });

    var hexDigits = new Array ("0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"); 

    function rgb2hex(rgb) {

        rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
        
        return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
    }

    function hex(x) {

        return isNaN(x) ? "00" : hexDigits[(x - x % 16) / 16] + hexDigits[x % 16];

    }

});    