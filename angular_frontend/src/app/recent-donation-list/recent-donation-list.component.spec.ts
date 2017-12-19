import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentDonationListComponent } from './recent-donation-list.component';

describe('RecentDonationListComponent', () => {
  let component: RecentDonationListComponent;
  let fixture: ComponentFixture<RecentDonationListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecentDonationListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecentDonationListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
