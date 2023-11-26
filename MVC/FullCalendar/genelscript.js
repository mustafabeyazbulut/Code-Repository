function LoadCalendarSearchUser(url, div,drag) {
    console.log ("dene");

    Metronic.blockUI({
        message: "Lütfen bekleyiniz...",
        boxed: true
    });
    $("#" + div).html("");

    $.post(url, function (data) {
        $("#" + div).html(data);
        Metronic.unblockUI();
        var draggableUsers = document.querySelectorAll("." + drag);
        draggableUsers.forEach(function (item) {
            // Sürüklenen öğeleri etkin hale getirin
            item.draggable = true;
            item.addEventListener('dragstart', function (event) {
                event.dataTransfer.setData('text/plain', item.dataset.itemId);

            });
        });
        $("#" + div).show();
    });

}