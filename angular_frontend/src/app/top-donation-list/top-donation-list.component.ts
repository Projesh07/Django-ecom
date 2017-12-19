import { Component, OnInit } from '@angular/core';
import {CampaignService} from '../campaign.service';
import {TopDonations} from '../campaign-model';
@Component({
  selector: 'top-donation-list',
  templateUrl: './top-donation-list.component.html',
  styleUrls: ['./top-donation-list.component.css']
})
export class TopDonationListComponent implements OnInit {

  top_donations: TopDonations[];
  constructor(private campaignslist: CampaignService){
   }

  ngOnInit() {
    this.getTopDonations();
  }

    getTopDonations(): void {
    this.campaignslist.getTopDonations()
          .subscribe(top_donations => {
           this.top_donations = top_donations;
           console.log('data',top_donations);
        });
	}
}
