// var form = $("#example-advanced-form").show();
// //$('#wizard').show();
 
// form.steps({
//     headerTag: "h4",
//     bodyTag: "fieldset",
//     transitionEffect: "slideLeft",
//     onStepChanging: function (event, currentIndex, newIndex)
//     {
//         // Allways allow previous action even if the current form is not valid!
//         if (currentIndex > newIndex)
//         {
//             return true;
//         }
//         // Forbid next action on "Warning" step if the user is to young
//         if (newIndex === 3 && Number($("#age-2").val()) < 18)
//         {
//             return false;
//         }
//         // Needed in some cases if the user went back (clean up)
//         if (currentIndex < newIndex)
//         {
//             // To remove error styles
//             form.find(".body:eq(" + newIndex + ") label.error").remove();
//             form.find(".body:eq(" + newIndex + ") .error").removeClass("error");
//         }
//         form.validate().settings.ignore = ":disabled,:hidden";
//         return form.valid();
//     },
//     onStepChanged: function (event, currentIndex, priorIndex)
//     {
//         // Used to skip the "Warning" step if the user is old enough.
//         if (currentIndex === 2 && Number($("#age-2").val()) >= 18)
//         {
//             form.steps("next");
//         }
//         // Used to skip the "Warning" step if the user is old enough and wants to the previous step.
//         if (currentIndex === 2 && priorIndex === 3)
//         {
//             form.steps("previous");
//         }
//     },
//     onFinishing: function (event, currentIndex)
//     {
//         // form.validate().settings.ignore = ":disabled";
//         return form.valid();
//     },
//     onFinished: function (event, currentIndex)
//     {
//         var form = $(this);

//             // Submit form input

//             form.submit();
//     }
// }).validate({
//     errorPlacement: function errorPlacement(error, element) { element.before(error); },
//     rules: {
//         confirm: {
//             equalTo: "#password-2"
//         }
//     }
// });

$('#wizard_load').show();


  // $(document).ready(function() {
        var max_fields      = 10;
        var wrapper         = $(".container1");
        var add_button      = $(".add_form_field");


    


        var selected_val=$('#id_content_type :selected').text()
        //option_selct(selected_val)
        $('#id_content_type').change(function(){
                selected_val=$('#id_content_type :selected').text();
                 $(wrapper).html('');
              
                //option_selct(selected_val)
        });
  

        // function option_selct(val){
       
        //     if(val=='Image' || val=='File'){

        //         console.log('File')

        //     }else{
        //         console.log('Others')
        //     }
        // }
       
        var x = 0;
        $(add_button).click(function(e){
            e.preventDefault();

            if(x < max_fields){
                x++; 

                // $(wrapper).append('<div><label for="id_content_link">Link '+x+':</label><input type="text" class="form-control" name="link[]"/><a href="#" class="delete">Delete</a></div>');
                $(wrapper).append('<div class="form-inline" style="margin: 5px auto;"><div class="form-group"><input type="text" class="form-control" name="link[]" placeholder="Link '+x+'"><span class="delete" style=""><i class="fa fa-trash-o" aria-hidden="true"></i></span></div></div>');  //add input box
                // if(selected_val=='Image' || selected_val=='File'){

                //     $(wrapper).append('<div><label for="id_content_link">'+selected_val+''+x+':</label><input type="file" class="form-control-none" name="document[]"/><a href="#" class="delete">Delete</a></div>'); //add input box
                // }else{
                //     $(wrapper).append('<div><label for="id_content_link">'+selected_val+''+x+':</label><input type="text" class="form-control" name="link[]"/><a href="#" class="delete">Delete</a></div>'); //add input box
                // }
            }
      else
      {
      alert('You Reached the limits')
      }
        });

        $(wrapper).on("click",".delete", function(e){
            e.preventDefault(); $(this).parent('div').remove(); x--;
        })
    // });


