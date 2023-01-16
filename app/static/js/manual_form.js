//ロードしたときの表示・非表示を設定
document.querySelector(".websiteSelect").style.display = "none";
document.querySelector(".author").style.display = "";
//querySelectorの引数にclass名を取得し、inputとlabel丸ごと表示非表示する
document.querySelector(".year").style.display = "";
document.querySelector(".title").style.display = "";
document.querySelector(".magazine").style.display = "none";
document.querySelector(".ifPublisherIsCheckbox").style.display = "none";
document.querySelector(".publisher").style.display = "";
document.querySelector(".ifVolumeIsCheckbox").style.display = "none";
document.querySelector(".volume").style.display = "none";
document.querySelector(".ifIssueIsCheckbox").style.display = "none";
document.querySelector(".issue").style.display = "none";
document.querySelector(".page").style.display = "";
document.querySelector(".url").style.display = "none";
//表示した各要素のplaceholderを任意に設定（ここでは書籍の例を表示している。）
document.getElementById("authorSubLabel").textContent = "例) カール・マルクス, エンゲルス[編]";
document.getElementById("yearSubLabel").textContent= "例) 1969";
document.getElementById("tiltleSubLabel").textContent= "例) 資本論(マルクス)1";
document.getElementById("publisherSubLabel").textContent= "例) 岩波文庫 白 125-1";
document.getElementById("pageSubLabel").textContent= "例) 307";

//----------
document.getElementById("format-select").addEventListener('change', function(){
//セレクトフォームを変更したとき、その値に応じて著者などの要素を出力する
  var selectedValue = document.getElementById("format-select").value;
  if (selectedValue == 1){
//全6パターン
    document.querySelector(".websiteSelect").style.display = "none";
    document.querySelector(".author").style.display = "";
    document.querySelector(".year").style.display = "";
    document.querySelector(".title").style.display = "";
    document.querySelector(".magazine").style.display = "none";
    document.querySelector(".ifPublisherIsCheckbox").style.display = "none";
    document.querySelector(".publisher").style.display = "";
    document.querySelector(".ifVolumeIsCheckbox").style.display = "none";
    document.querySelector(".volume").style.display = "none";
    document.querySelector(".ifIssueIsCheckbox").style.display = "none";
    document.querySelector(".issue").style.display = "none";
    document.querySelector(".page").style.display = "";
    document.querySelector(".url").style.display = "none";
    
    document.getElementById("authorSubLabel").textContent= "カール・マルクス, エンゲルス[編]";
    document.getElementById("yearSubLabel").textContent= "1969";
    document.getElementById("tiltleSubLabel").textContent= "資本論(マルクス)1";
    document.getElementById("publisherSubLabel").textContent= "岩波文庫 白 125-1";
    document.getElementById("pageSubLabel").textContent= "307";

  } else if (selectedValue == 2) {
          //日本語の論文
    document.querySelector(".websiteSelect").style.display = "none";
    document.querySelector(".author").style.display = "";
    document.querySelector(".year").style.display = "";
    document.querySelector(".title").style.display = "";
    document.querySelector(".magazine").style.display = "";
    document.querySelector(".ifPublisherIsCheckbox").style.display = "none";
    document.querySelector(".publisher").style.display = "";
    document.querySelector(".ifVolumeIsCheckbox").style.display = "";
    document.querySelector(".volume").style.display = "";
    document.querySelector(".ifIssueIsCheckbox").style.display = "";
    document.querySelector(".issue").style.display = "";
    document.querySelector(".page").style.display = "";
    document.querySelector(".url").style.display = "";

    document.getElementById("authorSubLabel").textContent = "例) 山田 昌弘";
    document.getElementById("yearSubLabel").textContent= "例) 2013";
    document.getElementById("tiltleSubLabel").textContent= "例) 日本家族のこれから";
    document.getElementById("magazineSubLabel").textContent= "例) 社会学評論";
    document.getElementById("publisherSubLabel").textContent= "例) 日本社会学会";
    document.getElementById("volumeSubLabel").textContent= "例) 64";
    document.getElementById("issueSubLabel").textContent= "例) 4";
    document.getElementById("pageSubLabel").textContent= "例) 649-662";
    document.getElementById("urlSubLabel").textContent= "例) https://doi.org/10.4057/jsr.64.649 (※論文ではURLが必須ではありません)";
  } else if (selectedValue == 3) {
    //日本語のWEBサイト
    document.querySelector(".websiteSelect").style.display = "";
    document.querySelector(".author").style.display = "";
    document.querySelector(".year").style.display = "";
    document.querySelector(".title").style.display = "";
    document.querySelector(".magazine").style.display = "none";
    document.querySelector(".ifPublisherIsCheckbox").style.display = "";
    document.querySelector(".publisher").style.display = "";
    document.querySelector(".ifVolumeIsCheckbox").style.display = "none";
    document.querySelector(".volume").style.display = "none";
    document.querySelector(".ifIssueIsCheckbox").style.display = "none";
    document.querySelector(".issue").style.display = "none";
    document.querySelector(".page").style.display = "none";
    document.querySelector(".url").style.display = "";

    document.getElementById("authorSubLabel").textContent= "例) 宗金 建志";
    document.getElementById("yearSubLabel").textContent= "例) 2022, 9, 8";
    document.getElementById("tiltleSubLabel").textContent= "例) 中国の人口が減少、2023年にはインドが世界首位:国連予測例) 国民経済計算(GDP統計) 2022年4-6月期・2次速報(2022年9月8日)";
    document.getElementById("publisherSubLabel").textContent= "日本貿易振興機構";
  document.getElementById("urlSubLabel").textContent= "例) https://www.jetro.go.jp/biz/areareports/2022/db12433a352ecc90.html";
  } else if (selectedValue == 4) {
    //英語の書籍
    document.querySelector(".websiteSelect").style.display = "none";
    document.querySelector(".author").style.display = "";
    document.querySelector(".year").style.display = "";
    document.querySelector(".title").style.display = "";
    document.querySelector(".magazine").style.display = "none";
    document.querySelector(".ifPublisherIsCheckbox").style.display = "none";
    document.querySelector(".publisher").style.display = "";
    document.querySelector(".ifVolumeIsCheckbox").style.display = "none";
    document.querySelector(".volume").style.display = "none";
    document.querySelector(".ifIssueIsCheckbox").style.display = "none";
    document.querySelector(".issue").style.display = "none";
    document.querySelector(".page").style.display = "none";
    document.querySelector(".url").style.display = "none";

    document.getElementById("authorSubLabel").textContent= "例) Marx, K";
    document.getElementById("yearSubLabel").textContent= "例) 1996";
    document.getElementById("tiltleSubLabel").textContent= "例) Das Kapital(F. Engels, Ed.)";
    document.getElementById("publisherSubLabel").textContent= "例) Regnery Publishing";
  } else if (selectedValue == 5) {
    //英語の論文
    document.querySelector(".websiteSelect").style.display = "none";
    document.querySelector(".author").style.display = "";
    document.querySelector(".year").style.display = "";
    document.querySelector(".title").style.display = "";
    document.querySelector(".magazine").style.display = "";
    document.querySelector(".ifPublisherIsCheckbox").style.display = "none";
    document.querySelector(".publisher").style.display = "";
    document.querySelector(".ifVolumeIsCheckbox").style.display = "";
    document.querySelector(".volume").style.display = "";
    document.querySelector(".ifIssueIsCheckbox").style.display = "";
    document.querySelector(".issue").style.display = "";
    document.querySelector(".page").style.display = "";
    document.querySelector(".url").style.display = "";

    document.getElementById("authorSubLabel").textContent= "例) Hardin, G (名, 姓)";
    document.getElementById("yearSubLabel").textContent= "例) 1968";
    document.getElementById("tiltleSubLabel").textContent= "例) The Tragedy of the Commons";
    document.getElementById("magazineSubLabel").textContent= "例) Science";
    document.getElementById("publisherSubLabel").textContent= "例) American Association for the Advancement of Science";
    document.getElementById("volumeSubLabel").textContent= "例) 162";
    document.getElementById("issueSubLabel").textContent= "例) 3859";
    document.getElementById("pageSubLabel").textContent= "例) 1243-1248";
    document.getElementById("urlSubLabel").textContent= "例) https://doi.org/10.1126/science.162.3859.1243 (※論文ではURLが必須ではありません)";
  } else{
    //英語のWEBサイト
    //例　Author Last Name, First initial. (Year, Month Date Published). Title of web page. Name of Website. URL
    document.querySelector(".websiteSelect").style.display = "";
    document.querySelector(".author").style.display = "";
    document.querySelector(".year").style.display = "";
    document.querySelector(".title").style.display = "";
    document.querySelector(".magazine").style.display = "none";
    document.querySelector(".ifPublisherIsCheckbox").style.display = "";
    document.querySelector(".publisher").style.display = "";
    document.querySelector(".ifVolumeIsCheckbox").style.display = "none";
    document.querySelector(".volume").style.display = "none";
    document.querySelector(".ifIssueIsCheckbox").style.display = "none";
    document.querySelector(".issue").style.display = "none";
    document.querySelector(".page").style.display = "none";
    document.querySelector(".url").style.display = "";

    document.getElementById("authorSubLabel").textContent= "例) Illing, S (名, 姓)";
    document.getElementById("yearSubLabel").textContent= "例) 2019, November 9";
    document.getElementById("tiltleSubLabel").textContent= "例) Bullshit jobs: why they exist and why you might have one (斜線)";
    document.getElementById("publisher").textContent= "例) Vox (Possible exist)";
    document.getElementById("urlSubLabel").textContent= "例) https://www.vox.com/2018/5/8/17308744/bullshit-jobs-book-david-graeber-occupy-wall-street-karl-marx";
  }
});

//参考:https://magazine.techacademy.jp/magazine/24063
//    http://5am.jp/javascript/form_change_javascript/
//    Event.currentTargetとEvent.targetの違いについて(JavaDrove)

//-----publisher, volume, issue display or not func
var publisher_checkbox = document.getElementById('publisherCheckbox')
publisher_checkbox.addEventListener('change', function(){
//チェックボックスが入力されたら、publisherを表示する　逆に非表示する
//背景 ウェブサイトによって監修者がおらず、著者になっていることが考えられるため。
  if (publisher_checkbox.checked){
    document.querySelector(".publisher").style.display = "";
    console.log('display=blockが実行されました');
  } else {
    document.querySelector(".publisher").style.display = "none";
    console.log('display=none');
  }
});

var volume_checkbox = document.getElementById('volumeCheckbox')
volume_checkbox.addEventListener('change', function(){
//チェックボックスが入力→volumeを表示するor非表示する
  if (volume_checkbox.checked){
    document.querySelector(".volume").style.display = "";
    console.log('display=blockが実行されました');
  } else {
    document.querySelector(".volume").style.display = "none";
    console.log('display=none');
  }
});

var issue_checkbox = document.getElementById('issueCheckbox')
issue_checkbox.addEventListener('change', function(){
//チェックボックスが入力→issueを表示するor非表示する
  if (issue_checkbox.checked){
    document.querySelector(".issue").style.display = "";
    console.log('display=blockが実行されました');
  } else {
    document.querySelector(".issue").style.display = "none";
    console.log('display=none');
  }
});

//---- reset all input----
var reset_button = document.getElementById('reset');
reset_button.addEventListener('click', function(){
  document.getElementById("author").setAttribute('value','');
  document.getElementById("year").setAttribute('value','');
  document.getElementById("title").setAttribute('value','');
  document.getElementById("magazine").setAttribute('value','');
  document.getElementById("publisher").setAttribute('value','');
  document.getElementById("volume").setAttribute('value','');
  document.getElementById("issue").setAttribute('value','');
  document.getElementById("page").setAttribute('value','');
  document.getElementById("url").setAttribute('value','');
  document.getElementById("formGroup").setAttribute('value','');
});

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
    console.log("https://webfrontend.ninja/js-clipboard-write/")
    console.log("https://blog.hirokiky.org/entry/2022/01/26/161113")
    await copyMessage();
  } catch (error) {
    console.log(error + 'コピーするものがありません');
  }
};
async function copyMessage(){
  console.log('copyiconAppendedText changed');
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