import { Component, OnInit,Input } from '@angular/core';

@Component({
  selector: 'top-donation',
  templateUrl: './top-donation.component.html',
  styleUrls: ['./top-donation.component.css']
})
export class TopDonationComponent implements OnInit {

@Input() donar_name;
@Input() donate_time;
@Input() donate_amount;
  constructor() { }

  ngOnInit() {
  }

}
