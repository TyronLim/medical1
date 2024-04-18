$(function(){
    $.ajax({
        url:"http://127.0.0.1:5500/students/json/stu_score.json",
        type:"get",
        data:{},
        dataType:"json",
        success:function(data){
            let h_data = "";

            for(let i=0; i<10; i++){

                h_data+="<tr>";
                h_data+="<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                h_data+="<td>1</td>";
                h_data+="<td>홍길동</td>";
                h_data+="<td>100</td>";
                h_data+="<td>100</td>";
                h_data+="<td>100</td>";
                h_data+="<td>300</td>";
                h_data+="<td>100</td>";
                h_data+="<td>1</td>";
                h_data+="<td><button class='delBtn'>삭제</button></td>";
                h_data+="";
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    


            }


        },
        error:function(data){
            alert('error')
        }





    });//ajax



});//jquery