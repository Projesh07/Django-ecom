function attachFileReader(fileInput)
{
  if (window.FileReader) {
    var reader = new FileReader();
    reader.onload = function (e) {
      // alert($(fileInput).attr('id'));
      // alert('o')
      console.log(fileInput.files[0].size);
      // if (parseInt(fileInput.files[0].size) > 1000000) {
      //     alert('Maximální povolená velikost obrázku je 1 MB');
      //     return;
      // }
      fileInputName = 'image[]';  
      
      // if($(fileInput).attr('id') == 'product_pdf[]'){
      //   fileInputName = 'product_pdf[]'; 
      //   $(fileInput).siblings('.preview').append($('<img></img>').attr('src', BASE_URL + 'assets/img/pdfs.png').width(100));
      
      // }else {
        $(fileInput).siblings('.preview').append($('<img></img>').attr('src', e.target.result).width(100));
      // }
      

      /*and now add one more*/
      var next = $('<div></div>').addClass('one-photo');
      var preview = $('<div></div>').addClass('preview');
      var icon = $('<i></i>').addClass('fa fa-plus');

      var input = $('<input></input>').attr('type', 'file').addClass('fileUpload').attr('name', fileInputName).attr('id',fileInputName);
     
      var removeThisPicture = $('<div></div>').addClass('removePhoto').html('x').click(function (e)
      {
          if ((r = confirm('sure remove?') ) == true ) {

              ajax_file_delete(this);
              return;

              e.preventDefault();
              next.remove();

          }
      });
      next.append(input);
      next.append(removeThisPicture);
      next.append(icon);
      next.append(preview);
      $(fileInput).parent('.one-photo').after(next);
      input.change(function () {
        attachFileReader(this);
      });
    };
    reader.readAsDataURL($(fileInput) [0].files[0]);
  } 
  else
  {
    fileInputName = 'image[]';  

    if($(fileInput).attr('id') == 'document[]'){
      fileInputName = 'document[]'; 
    }
      
    var next = $('<div></div>').addClass('one-photo');
    var preview = $('<div></div>').addClass('preview');
    var input = $('<input></input>').attr('type', 'file').addClass('fileUpload').attr('name', fileInputName).attr('id',fileInputName);
     
    input.change(function () {
      attachFileReader(this);
    });
    var removeThisPicture = $('<div></div>').addClass('removePhoto').html('x').click(function (e)
    {
        if ((r = confirm('sure remove?') ) == true ) {

          ajax_file_delete(this);
          return;

          e.preventDefault();
          next.remove();
        }
    });
    var icon = $('<i></i>').addClass('fa fa-plus');
    next.append(input);
    next.append(removeThisPicture);
    next.append(icon);
    next.append(preview);
    $(fileInput).parent('.one-photo').after(next);
  }
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


function ajax_file_delete(el,csrftoken) {
    var file_id = $(el).data('file-id');

    console.log( BASE_URL );
    // console.log( {{ request.host }} );

    if (file_id != "") {

        $.ajax(
        {
            url: BASE_URL + 'admin/ajax_document_delete',
            type: 'post',
            data: {'file_id': file_id},
            dataType: 'json',
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function (response) {
                
                console.log(response);
             
            },
            error: function (request, status, error) {
                console.log("error setting url");
            }
        });

    }
}

$(function(){



    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    $('.removePhoto').on("click",function(){
        if ((r = confirm('sure remove?') ) == true ) {
            ajax_file_delete(this, csrftoken);
            // return;
            $(this).parent('.one-photo').remove();
        }
    });
});

