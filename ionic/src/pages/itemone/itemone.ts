import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, PopoverController } from 'ionic-angular';

import { PopoverPage } from '../popover/popover';

import { ProductProvider } from '../../providers/product/product';

@IonicPage()
@Component({
  selector: 'page-itemone',
  templateUrl: 'itemone.html',

})

export class ItemonePage {
  selectedData:any;
  data:any;
  constructor(public navCtrl: NavController, 
  	public navParams: NavParams, 
  	public popoverCtrl: PopoverController,
    private ProductProvider: ProductProvider) {
  }
  ionViewDidLoad() {
    // console.log('ionViewDidLoad ItemonePage');
  }
  presentPopover(myEvent) {
    let listData = [{title:"KOREA",id:1},{title:"JAPAN",id:2},{title:"CHINA",id:3},{title:"UNITESTATE",id:4}]
    let popover = this.popoverCtrl.create(PopoverPage, { listData });
    popover.present({
      ev: myEvent
    });
    popover.onDidDismiss(data => {
      if(data!=null){
         this.selectedData = data.title
      }
      else{
        this.selectedData = "DESTINATION"
      }
      console.log(this.selectedData)
    });
  }
  ionViewWillEnter(){
    this.ProductProvider.getItemList().subscribe(data => {
      this.data = data
      console.log(this.data)
    });
  }
}
