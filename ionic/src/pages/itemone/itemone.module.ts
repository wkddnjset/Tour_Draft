import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { ItemonePage } from './itemone';

@NgModule({
  declarations: [
    ItemonePage,
  ],
  imports: [
    IonicPageModule.forChild(ItemonePage),
  ],
})
export class ItemonePageModule {}
