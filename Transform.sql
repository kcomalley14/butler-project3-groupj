select * from "ZillowData"
 where "State" <>  'in'
 
delete from "ZillowData"
 where "State" <>  'in'
 
 select * from "ZillowData"
 where "State" = 'in'


ALTER TABLE "ZillowData" 
renanme  COLUMN "0" to "HomeValue";

ALTER TABLE public."ZillowData"
    ALTER COLUMN "RegionName" TYPE text;
	
 
ALTER TABLE "ZillowData" 
rename  COLUMN "filed_9" to "DateValue";

 