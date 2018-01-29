import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, AlertController} from 'ionic-angular';
import { TabsPage } from '../tabs/tabs';

import { ApitestProvider } from '../../providers/apitest/apitest';

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {
  response:any={}
  login:any = {}
  constructor(public navCtrl: NavController, 
  			  public navParams: NavParams,
  			  public alertCtrl: AlertController,
  			  private apitest : ApitestProvider,) {
  this.login.username = '';
  this.login.password = '';
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
  }

  login_function(){
	 this.apitest.postToken(this.login.username, this.login.password).subscribe(token => {
        this.response = token;
        let alert = this.alertCtrl.create({
        	title:"로그인에 성공하였습니다.",
        	message: this.response.token,
        	buttons: [
        	  {
        	  	text: 'OK',
        	  	role: 'OK',
        	  	handler: () => {
        	  		this.navCtrl.push(TabsPage, {token : this.response.token});
        	  	}
        	  }
        	]
        });
        alert.present();
    }, error => {
    	let alert = this.alertCtrl.create({
    		title: "로그인에 실패하였습니다.",
    		buttons:[
 			  {
 			  	text: 'OK',
        	  	role: 'OK',
        	  	handler: () => {
        	  	}
 			  }
    		]
    	});
    	alert.present();
    });
  }
}
