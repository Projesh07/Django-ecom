import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TopDonationListComponent } from './top-donation-list.component';

describe('TopDonationListComponent', () => {
  let component: TopDonationListComponent;
  let fixture: ComponentFixture<TopDonationListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TopDonationListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TopDonationListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
