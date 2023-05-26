function dictExtend(dict1, dict2){
    for (let key in dict2){
        if(dict2.hasOwnProperty(key)){
            dict1[key] = dict2[key];
        }
    }
    return dict1;
}


function getTrData(tr) {
	let trData = {};
	let headers = $('table').find('th:not(:last)');
	tr.children(':not(:last)').each( function(i){
		let dataType = headers[i].getAttribute('id');
		trData[dataType] = $(this)[0].innerText;
	});
	return trData;
}


export function saveInHistory(tr, saveMode) {
    let save = {
        'mode': saveMode,
        'timestamp': new Date().getTime() / 1000,
        'productId': tr[0].dataset.productId,
    };

    $.ajax({
        method: 'post',
        url: saveInHistoryView,
        data: dictExtend(save, getTrData(tr)),
    });
}