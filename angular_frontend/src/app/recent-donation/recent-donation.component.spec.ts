import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentDonationComponent } from './recent-donation.component';

describe('RecentDonationComponent', () => {
  let component: RecentDonationComponent;
  let fixture: ComponentFixture<RecentDonationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RecentDonationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RecentDonationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
