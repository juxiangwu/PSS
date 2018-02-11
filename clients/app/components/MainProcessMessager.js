Ext.define('PSS.components.MainProcessMessager',{
	constructor:function(app){
		
		var ipc = require('electron').ipcRenderer
		//console.log(app.host)
		ipc.on('open-product-profile',function(event, arg){
			console.log('open-product-profile')
		});

		ipc.on('open-product-category',function(event, arg){
			console.log('open-product-category')
			openWindow('product-category-win')
		});

		ipc.on('open-product-supplier',function(event, arg){
			console.log('open-product-supplier')
		});

		ipc.on('open-product-query',function(event, arg){
			console.log('open-product-query')
		});

		ipc.on('open-retail-dashboard',function(event, arg){
			console.log('open-retail-dashboard')
		});

		ipc.on('open-retail-detail',function(event, arg){
			console.log('open-retail-detail')
		});

		ipc.on('open-retail-day-summary',function(event, arg){
			console.log('open-retail-day-summary')
		});

		ipc.on('open-retail-query',function(event, arg){
			console.log('open-retail-query')
		});

		ipc.on('open-repetory-dashboard',function(event, arg){
			console.log('open-repetory-dashboard')
		});

		ipc.on('open-repetory-detail',function(event, arg){
			console.log('open-repetory-detail')
		});

		ipc.on('open-repetory-query',function(event, arg){
			console.log('open-repetory-query')
		});

		ipc.on('open-repetory-check',function(event, arg){
			console.log('open-repetory-check')
		});

		ipc.on('open-repetory-check',function(event, arg){
			console.log('open-repetory-check')
		});

		ipc.on('open-repetory-check-record',function(event, arg){
			console.log('open-repetory-check-record')
		});

		ipc.on('open-repetory-exchange',function(event, arg){
			console.log('open-repetory-exchange')
		});

		ipc.on('open-repetory-exchange-record',function(event, arg){
			console.log('open-repetory-exchange-record')
		});

		ipc.on('open-department',function(event, arg){
			console.log('open-department')
		});

		ipc.on('open-role',function(event, arg){
			console.log('open-role')
		});

		ipc.on('open-employee-profile',function(event, arg){
			console.log('open-employee-profile')
		});

		ipc.on('open-authority',function(event, arg){
			console.log('open-authority')
		});

		ipc.on('open-employee-authority',function(event, arg){
			console.log('open-employee-authority')
		});

		function openWindow(wid){
			var module = app.getModule(wid)

			console.log(module)
			if(module){
				var win = app.createWindow(module)
			}else{
				console.log('cannot open window')
			}
		}

	},

	// openWindow:function(app,wid){
	// 	var module = app.getModule(wid)

	// 	console.log(module)
	// 	if(module){
	// 		var win = app.createWindow(module)
	// 	}else{
	// 		console.log('cannot open window')
	// 	}
	// }
})