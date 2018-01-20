import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { ApitestProvider } from '../../providers/apitest/apitest';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  api_id : any;

  constructor(public navCtrl: NavController, private apitest : ApitestProvider) {

  }
    ionViewWillEnter(){
    	this.api_id = '1'
    	this.apitest.getApi(this.api_id).subscribe(api => {
    		console.log(api);
    	});
    }

}
