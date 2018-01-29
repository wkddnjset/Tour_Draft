import { Component } from '@angular/core';
import { NavController, NavParams } from 'ionic-angular';
import { ApitestProvider } from '../../providers/apitest/apitest';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  image:any;
  pk : string;
  token:any;

  constructor(
    public navCtrl: NavController, 
    private navPar: NavParams,
    private apitest : ApitestProvider) {
  }
  ionViewDidLoad() {
    console.log('ionViewDidLoad HomePage');
    this.token =  this.navPar.data.token;
    console.log(this.token);
  }
  ionViewWillEnter(){
    this.pk = "1";
  	this.apitest.getImage(this.pk, this.token).subscribe(api => {
      console.log(api);
      this.image = api;
  	});
  }
}