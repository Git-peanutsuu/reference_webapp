//old version that I used.
// var copy_button = document.getElementById("result_copy_button");
// copy_button.addEventListener('click', function(){
//   /* コピーボタンをclickしたときの処理　*/
//   var copyText = document.getElementById("formtargetResultTextarea").textContent;
//   var copyHTML = document.getElementById("formtargetResultTextarea").innerHTML;
//   copytoClipboard(copyText,copyHTML);
// });
// async function copytoClipboard(copyTarget,copyHTML){
//   /* navigator returns Promiss. Thus async function is used here*/
//   /* refer to https://www.marorika.com/entry/copy-to-clipboard*/
//   try {
//     /* Get the text field */
    
//     const copy_item = new ClipboardItem({
//     // HTMLとプレーンテキストに対応し、ペーストが両方のフォーマットで出力が可能に
//     'text/plain': new Blob([copyTarget], { type: 'text/plain' }),
//     'text/html': new Blob([copyHTML], { type: 'text/html' })
//     // blobオブジェクトとして返す
//     });
//     await navigator.clipboard.write([copy_item]);
//     console.log("https://webfrontend.ninja/js-clipboard-write/")
//     console.log("https://blog.hirokiky.org/entry/2022/01/26/161113")
//     await copyMessage();
//   } catch (error) {
//     console.log(error + 'コピーするものがありません');
//   }
// };
// async function copyMessage(){
//   // FIX clipboardせずに、カーソルを
//   console.log('copyorcopied');
//   document.getElementById('copyorcopied').innerText = "コピーしました";
//   // copy_button.addEventListener('mouseleave', makeTextOriginal());
//   copy_button.onmouseleave = makeTextOriginal;

//   function makeTextOriginal(){
//     document.getElementById('copyorcopied').innerText = "コピーする";
//     console.log('function makeTextOriginal');
//   };
// };



//Easy copy version of not using async.
// var submit_button = document.getElementById("submit")
// submit_button.addEventListener('click', function(){
//   //document.getElementById("format-select").selectedIndex = document.getElementById("format-select").value;
//   console.log(document.getElementById("format-select").selectedIndex)
// });
// https://teratail.com/questions/259060
// var copy_button = document.getElementById("result_copy_button");
// copy_button.addEventListener('click', ()=>{
//   /* Get the text field */
//   var copyText = document.getElementById("formtargetResultTextarea");
//     /* copyTextののオブジェクトはinputである必要があるのかも */
//   //textareやinput意外では、copyTextはobjectが返される
//   try{
//     /* Copy the text inside the text field */
//     navigator.clipboard.writeText(copyText.value);
//     console.log("Copied the text: " + copyText.value);
//   }catch{
//     console.log("コピーするものがありません")
//   }
// })
//TODO hrを下に書く