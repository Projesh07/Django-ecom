import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CampaingnPageComponent } from './campaingn-page.component';

describe('CampaingnPageComponent', () => {
  let component: CampaingnPageComponent;
  let fixture: ComponentFixture<CampaingnPageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CampaingnPageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CampaingnPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
