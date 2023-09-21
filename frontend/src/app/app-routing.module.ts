import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WelcomeComponent } from './components/welcome/welcome.component';
import { StockComponent } from './components/stock/stock.component';
import { LoginComponent } from './components/login/login.component';
import { RegistrationComponent } from './components/registration/registration.component';
import { CategoryComponent } from './components/category/category.component';
import { AddCategoryComponent } from './components/category/add-category/add-category.component';
import { ViewCategoryComponent } from './components/category/view-category/view-category.component';
import { EditCategoryComponent } from './components/category/edit-category/edit-category.component';

const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full' },
  {path: 'home', component: WelcomeComponent},
  {path: 'stocks', component: StockComponent},
  {path: 'category', component: CategoryComponent},
  { path: 'category/add-category', component: AddCategoryComponent },
  { path: 'view-category', component: ViewCategoryComponent },
  { path: 'edit-category/:id', component: EditCategoryComponent },
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegistrationComponent},
  // Routes for Category section
  {path: 'register', component: RegistrationComponent}
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
