import { Component, OnInit } from '@angular/core';
import {CampaignService} from '../campaign.service';
import {TopDonations} from '../campaign-model';

@Component({
  selector: 'donation-list',
  templateUrl: './donation-list.component.html',
  styleUrls: ['./donation-list.component.css']
})
export class DonationListComponent implements OnInit {

  recent_donations: TopDonations[];
  top_donations: TopDonations[];
  constructor(private campaignslist: CampaignService){
   }

  ngOnInit() {
    this.getRecentDonations();
    this.getTopDonations();
  }

    getRecentDonations(): void {
    this.campaignslist.getRecentDonations()
          .subscribe(recent_donations => {
           this.recent_donations = recent_donations;
           console.log('data',recent_donations);
        });
	}

	getTopDonations(): void {
    this.campaignslist.getTopDonations()
          .subscribe(top_donations => {
           this.top_donations = top_donations;
           console.log('data',top_donations);
        });
	}
}
