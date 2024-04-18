$(function(){





    //-----------------------------------------------새로입력 시작----------------------------------//
    $(document).on("click",".replyBtn",function(){
        $(".replyType").val()
        

    });// .replyBtn 
    

    //-----------------------------------------------새로입력 끝----------------------------------//



    //-----------------------------------------------불러오기 시작----------------------------------//
    $.ajax({
        url:"http://127.0.0.1:5500/event/event/json/comment_data.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            //alert('success');
            let h_data = "";
            for(let i=0;i<data.length;i++){
                h_data+='<ul id='+data[i].cno+'>'
                h_data+='<li class="name">'+data[i].id+' <span>['+data[i].cdate+'&nbsp;&nbsp;15:01:59]</span></li>'
                h_data+='<li class="txt">'+data[i].ccont+'</li>'
                h_data+='<li class="btn">'
                h_data+='<a href="#" class="rebtn updateBtn">수정</a>'
                h_data+='<a href="#" class="rebtn delBtn">삭제</a>'
                h_data+='</li>'
                h_data+='</ul>'
            }
            $(".replyBox").html(h_data); 
        },
        error:function(data){
            alert('error');
        } 
    });//ajax
    //-----------------------------------------------불러오기 끝----------------------------------//


});// query