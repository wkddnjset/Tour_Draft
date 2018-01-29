import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

/*
  Generated class for the ApitestProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class ApitestProvider {
  url;

  constructor(public http: HttpClient) {
    console.log('Hello ApitestProvider Provider');
    this.url = 'http://localhost:8000/api/test/'
  }
  getApi(pk){
  	return this.http.get('img/'+this.url+pk+'/?format=json')
  }
  postSignup(username, email, password){
    return this.http.post(this.url+'signup/',
      { "username":username, "email":email, "password":password},
      { headers: { 'Content-Type': 'application/json' } }
      )
  }
  postToken(username, password){
    return this.http.post( this.url+'auth/token/',
      { "username":username, "password":password},
      { headers: { 'Content-Type': 'application/json' } }
      )
  }
  getImage(pk, token){
    return this.http.get(this.url+'img/'+pk+'/?format=json', 
      {headers:{
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + token }
      })
  }
}
