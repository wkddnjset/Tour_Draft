import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, AlertController } from 'ionic-angular';
import { WelcomePage } from '../welcome/welcome'
import { ApitestProvider } from '../../providers/apitest/apitest';
import { FormGroup, FormBuilder, Validators } from "@angular/forms";

/**
 * Generated class for the SignupPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-signup',
  templateUrl: 'signup.html',
})
export class SignupPage {
  authForm : FormGroup;
  signup:any = {}
  response:any = {}
  constructor(public navCtrl: NavController, 
  			  public navParams: NavParams, 
  			  public alertCtrl: AlertController,
  			  private apitest : ApitestProvider,
          private fb: FormBuilder) {
  this.signup.username = '';
  this.signup.email = '';
  this.signup.password = '';
  this.authForm = fb.group({
      'username'  : [null, Validators.compose([Validators.required, Validators.minLength(8)])],
      'email'     : [null, Validators.compose([Validators.required, Validators.minLength(8)])],
      'password'  : [null, Validators.compose([Validators.required, Validators.minLength(8)])],
    });
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad SignupPage');
  }

  signup_function(){
	 this.apitest.postSignup(this.signup.username, this.signup.email, this.signup.password).subscribe(response => {
        this.response = response;
        let alert = this.alertCtrl.create({
        	title:"회원가입 되었습니다.",
        	message: this.response.email,
        	buttons: [
        	  {
        	  	text: 'OK',
        	  	role: 'OK',
        	  	handler: () => {
        	  		this.navCtrl.push(WelcomePage);
        	  	}
        	  }
        	]
        });
        alert.present();
    }, error => {
    	let alert = this.alertCtrl.create({
    		title: "다른 아이디로 회원가입 해주세요.",
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


  // ionViewVillEnter(){

  // 	this.signup_data = {
  // 		username :'test',
  // 		email : 'test@gmail.com',
  // 		password : 'test'
  // 	}

  // 	this.ApitestProvider.postsignup(this.signup_data.username,
  // 									this.signup_data.email,
  // 									this.signup_data.password).subscribe(message => {
  // 										console.log(message);
  // 									});
  // }
}
