// Select All Function
function toggle(source) {
    checkboxes = document.getElementsByName('check_box');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
  }