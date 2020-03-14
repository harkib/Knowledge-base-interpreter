Choose which of the worlds top 13 Cities in AI and engineering you should live in (after graduating).

Are you well off? Tell the atoms below that apply to you, then infer_all

--------------------- non-students
good_career
tech_job
hard_worker
smart
no_student_loan
no_car_loan
--------------------- students 
part_time_job
CS_grad
good_communication
sfu_open_scholarship
high_gpa 
hard_worker
smart

Theres no point in living in an expesive city if you don't utilize its suroundings. 
Tell the atoms below that apply to you, then infer_all and see activites you might like

fit
can_swim
like_nature
like_adrenaline
like_snow
like_sun

Tell alteast one atom for each category that you would like, then infer_all and see cities 
1) continent: Asia, North_America, Europe
2) winter: mild_winter &, cold_winter & 
3) summer: mild_summer, hot_summer


See example below. 

kb>load a4_q2_kb.txt
   25 new rule(s) added

   Beijing <-- Asia & cold_winter & hot_summer & well_off & like_hiking
   Hong_kong <-- Asia & cold_winter & hot_summer & well_off & like_skiing
   San_Francisco <-- North_America & mild_winter & hot_summer & well_off & like_beach
   London <-- Europe & mind_winter & mild_summer
   Berlin <-- Europe & cold_winter & mild_summer
   New_York <-- North_America & cold_winter & hot_summer & well_off & like_hiking    
   Toronto <-- North_America & cold_winter & mild_summer
   Seattle <-- North_America & cold_winter & mild_summer
   Singapore <-- Asia & mind_winter & hot_summer & well_off & like_hiking
   Montreal <-- North_America & cold_winter & mild_summer
   Boston <-- North_America & cold_winter & hot_summer
   Amsterdam <-- Europe & mind_winter & mild_summer
   Tokyo <-- Europe & mind_winter & hot_summer & well_off & like_skiing
   well_off <-- good_career & no_loans
   good_career <-- tech_job & hard_worker & smart
   no_loans <-- no_student_loan & no_car_loan
   no_student_loan <-- sfu_open_scholarship
   no_car_loan <-- part_time_job
   part_time_job <-- hard_worker & smart
   tech_job <-- CS_grad & good_communication
   sfu_open_scholarship <-- high_gpa
   high_gpa <-- hard_worker & smart
   like_hiking <-- fit & like_nature
   like_beach <-- like_nature & can_swim & like_sun
   like_skiing <-- like_adrenaline & like_nature & like_snow

kb>tell hard_worker, smart, high_gpa, CS_grad, good_communication  
Error: "hard_worker," is not a valid atom
kb>tell hard_worker smart high_gpa CS_grad good_communication     
  "hard_worker" added to KB
  "smart" added to KB
  "high_gpa" added to KB
  "CS_grad" added to KB
  "good_communication" added to KB

kb>infer_all                                                 
  Newly inferrd atoms:
      part_time_job, no_car_loan, tech_job, good_career, sfu_open_scholarship, no_student_loan, no_loans, well_off
  Atoms already known to be true:
      hard_worker, smart, high_gpa, CS_grad, good_communication

kb>tell can_swim like_nature like_sun like_snow
  "can_swim" added to KB
  "like_nature" added to KB
  "like_sun" added to KB
  "like_snow" added to KB

kb>infer_all
  Newly inferrd atoms:
      like_beach
  Atoms already known to be true:
      hard_worker, smart, high_gpa, CS_grad, good_communication, part_time_job, no_car_loan, tech_job, good_career, sfu_open_scholarship, no_student_loan, no_loans, well_off, can_swim, 
like_nature, like_sun, like_snow

kb>tell Asia North_America Europe mild_winter cold_winter hot_summer
  "Asia" added to KB
  "North_America" added to KB
  "Europe" added to KB
  "mild_winter" added to KB
  "cold_winter" added to KB
  "hot_summer" added to KB

kb>infer_all
  Newly inferrd atoms:
      San_Francisco, Boston
  Atoms already known to be true:
      hard_worker, smart, high_gpa, CS_grad, good_communication, part_time_job, no_car_loan, tech_job, good_career, sfu_open_scholarship, no_student_loan, no_loans, well_off, can_swim, 
like_nature, like_sun, like_snow, like_beach, Asia, North_America, Europe, mild_winter, cold_winter, hot_summer
