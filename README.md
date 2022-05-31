# Vehicle Maintenance Logbook

## Overview
A web based vehicle maintenance logbook where mechanics can track their vehicle(s) maintenance, view upcoming maintenance tasks, and get information about their vehicle from their VIN. The purpose of this project was to make an application which can be viewed from any web connected device so the user can easily track the maintenance they have completed; it provides the ability to log the maintenance item, mileage at completion, date completed, as well as any notes the user wants to add about the maintenance. The project will be built using Django and Vue.js.

## Features
#### As a mechanic who performs my own automotive maintenance at home I want a simple way to record the maintenance that I have completed because it lets me know what day it was done and at what mileage, which helps with scheduling future maintenance and troubleshooting.

### Tasks
- Create model for users.
- Create a form to create a new user.
- Crate a model for the user's vehicle(s).
- Create a form for user to add a vehicle to their account.
- Create model for maintenance item (maintenance item, date, mileage, and notes).
- Create a form for the user to submit that has the maintenance information.
- Create a view that receives the form submissions, saves the maintenance to the database, and returns the logbook entries chronologically.
- Possibly implement the ability for the user to set custom intervals for the date/mileage until the specific maintenance item is due.


#### As a vehicle owner who does no maintenance I want to track the date, mileage, and price of maintenance performed on my vehicle because I want to compare future prices for jobs and to know when regularly scheduled maintenance will be due.

### Tasks
- Create date/mileage reminders (emails?) for upcoming maintenance or an additional column in the logbook which displays next date/mileage when the maintenance item is due.
- Possibly implement an email reminder system which can be set for when it is sent as a reminder for upcoming maintenance.

### Additional Features
- API to lookup vehicle information from Vehicle Identification Number (VIN).
- Standard vehicle maintenance intervals which will be applied to specific regularly scheduled maintenance (oil change, tire rotation, air filter change, etc.).

## Schema (Data Model)
- VehicleInformation
    - current_mileage (integer field)
    - year
    - make
    - model
    - nickname (user generated, optional)
    - regular maintenance intervals (inherited from standard, can be edited for each vehicle)
    - user (foreign key to user)
    
- MaintenanceItem
    - name of maintenance job
    - user (foreign key to user)
    - date (date completed)
    - mileage (mileage at completion)
    - notes (cost, shop name, other...)

## Schedule
### Week 1
    * Create and clone repo.
    * Create virtual environment.
    * Start Django project.
    * Write Django models.
    * Create MVP of vehicle selection and vehicle page after user login.

### Week 2
    * MVP of VIN lookup.
    * Organize display of completed maintenance items.
    * Calculate next maintenance interval using standard intervals for regular maintenance.
    * Possibly allow user to edit regular maintenance intervals, per vehicle.

### Week 3
    * Allow user to edit/delete maintenance posts.
    * Allow user to add/change/delete a photo of their vehicle for the vehicle page.
    * Work on styling app.

### Week 4
    * Deploy on heroku.
    * Additional styling of app.

## Feature Tiers
### Must Haves
- User login to see account/vehicle(s).
- Maintenance logbook for each vehicle within user account.
- Ability to add/edit/delete entered maintenance items.
- API for VIN lookup.
### Should Haves
- Upcoming Maintenance Interval
- Easy to use UI.
- Photo upload for vehicle page.
### Can Haves
- Ability to edit maintenance intervals per vehicle.
- Email reminder of upcoming maintenance due.
- Calendar
- Dark Mode
### Won't Haves
- Users able to see other users or their vehicles. (This is a private experience.)
