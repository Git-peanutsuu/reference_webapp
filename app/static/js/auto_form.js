//---copy result and change icon temporary
var copy_button = document.getElementById("result_copy_button");
copy_button.addEventListener('click', async function(){
  /* コピーボタンをclickしたときの処理　*/
  var copyText = document.getElementById("formtargetResultTextarea").textContent;
  var copyHTML = document.getElementById("formtargetResultTextarea").innerHTML;
   /* Get the text field */
  await copytoClipboard(copyText,copyHTML);
});
async function copytoClipboard(copyTarget,copyHTML){
  /* navigator returns Promiss. Thus async function is used here*/
  /* refer to https://www.marorika.com/entry/copy-to-clipboard*/
  try {
    const copy_item = new ClipboardItem({
    // HTMLとプレーンテキストに対応し、ペーストが両方のフォーマットで出力が可能に
    'text/plain': new Blob([copyTarget], { type: 'text/plain' }),
    'text/html': new Blob([copyHTML], { type: 'text/html' })
    // blobオブジェクトとして返す
    });
    await navigator.clipboard.write([copy_item]);
    await copyMessage();
  } catch (error) {
    console.log(error + 'コピーするものがありません');
  }
};
async function copyMessage(){
  console.log('copyorcopied');
  document.getElementById('copyiconAppendedText').innerText = "コピーしました!";
  document.getElementById('copyicon').className = "bi-clipboard-check"

  setTimeout(() => {makeTextOriginal()}, 2000)
  // DO NOT KNOW HOW IT WORKS 
  function makeTextOriginal(){
    document.getElementById('copyiconAppendedText').innerText = "コピーする";
    console.log('function makeTextOriginal');
    document.getElementById('copyicon').className = "bi-clipboard"
  };
};