prompt_templates = {
    "MTF": """Match the column
answer key - {answer_key}
 topic - 
 {topics}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions 
create 5 match the column type questions - very ugc net home science. remember to add the hence line at the end - important .  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. arrange the options such that the answer key is true. explain all major keywords in 1 setence each. longer and better explanation and dont type anything like topic or intro etc. just what i asked. remember to add the hence line at the end - important. the options should be one under the other and only 4 options. make sure you create 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens, and use this VERY EXACT format - with the top guideline being the exact same "Match the following:" - format -

--Question Starting--
1. Match the following with List I with List II
List: Food Equipment/Storage List II: Associated Risks
I. Can reformer (A)Areas of under-cooking, foodborne illness
II. Grain silo (B)Botulism due to damaged containers
III. Heat exchanger (C)Mould growth due to high moisture
IV. Pump (D)Spoilage of mayonnaise
V. Commercial oven (E) Salmonellosis from milk powder

(1) I – A, II – E, III – B, IV – C, V – D
(2) I – B, II – C, III – E, IV – D, V – A  
(3) I – C, II – D, III – A, IV – B, V – E
(4) I – E, II – B, III – D, IV – C, V – A
Answer Key: (2)
Solution:
Option I – B
Option II – C
Option III – E
Option IV – D
Option V – A 

Option I - Can reformer with holes can lead to Botulism (B). This is a severe foodborne illness caused by anaerobic bacteria in damaged cans.
Option II - Inadequate ventilation prevents proper air circulation, trapping moisture within the grain. Leaks can also introduce external moisture, by increasing the moisture in the stored grain. It creates an environment conducive to mould (C)growth and mycotoxin contamination.
Option III - A cracked heat exchanger can allow contaminated water to enter. It results in Salmonellosis from milk powder (E).
Option IV - A malfunctioning pump in a mayonnaise production line could lead to inconsistencies in the mixing or transfer of ingredients. By causing the emulsion to break down and the oil to separate, leading to an undesirable, watery texture. (D).
Option V - An improperly functioning commercial oven can have uneven heat distribution or fail to reach the required cooking temperatures. Poor heat distribution in a commercial oven can result in areas of under-cooking and potential foodborne illness (A).
Hence, the correct answer is Option (2).
""",

    "MCQ": """MCQ

answer key - {answer_key}
topic - 
{topics}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
create 5 mcq type questions with multiple being selected- very ugc net home science type . remember to add the hence line at the end - important. arrange the options such that the answer key is true. explain all major keywords in 1 setence each. longer and better explanation and dont type anything like topic or intro etc. just what i asked.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. remember that mcq type questions' options are always short and of only 1 to 4 words max. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens and use this exact format - 

--Question Starting--
1. Which raising agent releasing both carbon dioxide and ammonia without leaving any residue?
(1) Sodium Bicarbonate
(2) Potassium Carbonate
(3) Ammonium Bicarbonate
(4) Calcium Phosphate
Answer Key: (3)
Solution:
Option (3) is correct. Ammonium bicarbonate is particularly valued because it decomposes upon heating at around 60°C, releasing carbon dioxide and ammonia and leaving no residue in the baked product. This is suitable for products like cookies, crackers, and cream puffs.
Option (1) is incorrect. Sodium bicarbonate releases carbon dioxide.
Option (2) is incorrect. Potassium carbonate requires an acid to release carbon dioxide and is less convenient to use. It doesn't release ammonia.
 Option (4) is incorrect. Calcium phosphate is a slow-acting acid component in baking powders but does not release gases.
Hence, the correct answer is Option (3).
""",
    "2S": """2 statement type
topics - 
{topics}
. answer keys - {answer_key}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
arrange the options such that the answer key is true. create 5 - 2 statement type questions like this - very ugc net typehome science, and very analytical. a lot longer and better explanation and explain all major keywords in 1 setence each and dont type anything like topic name or intro etc. just what i asked.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. remember to add the hence line at the end - important. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens and use this VERY exact format -

--Question Starting--
1. Read the following statements and choose the correct option.
Statement I: As corn oil has a high percentage of polyunsaturated fat and a low percentage of saturated fat, it is regarded as healthful.
Statement II: Castor oil is a good choice for everyday cooking due to its mild flavour and low viscosity.
Choose the correct answer from the options below:
(1) Statement I is correct, and Statement II is incorrect
(2) Statement I is incorrect, and Statement II is correct
(3) Both statements are incorrect
(4) Both statements are correct
Answer Key: (1)
Solution:
Statement I is correct. Because of its low saturated fat content and high content of polyunsaturated fatty acids (PUFAs), corn oil is in fact a healthy edible oil.
Statement II is incorrect. Castor oil, however, is not used for cooking due to its thicker viscosity and specific taste.
Hence, the correct answer is Option (1).""",

    "3S" : """"3 statement type
answer key - {answer_key}
topics - 
{topics}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
create 5 - 3 statement type questions - - very ugc net home science type, and very analytical. arrange the options such that the answer key is true. very very long and better explanation and explain all major keywords in 1 setence eac and dont type anything like topic or intro etc. remember to add the hence line at the end - important.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. just what i asked. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens - format -

--Question Starting--
1. Identify the key roles of packaging in the modern socio-scientific discipline from the following list:
I. Protecting against biological and chemical damages
II. Increasing shelf-life and availability
III. Disposal without environmental responsibility
Choose the correct answer from the options given below:
(1) I, II, III Only
(2) I, II Only
(3) I, III Only
(4) II, III Only
Answer Key: (2)
Solution:
Statement I is correct. Packaging plays a critical role in protecting products against biological, chemical, and distribution damages.
Statement II is correct. One of the major functions of packaging is to increase the shelf-life of products and ensure their availability for a longer time.
Statement III is incorrect because packaging emphasizes environmental responsibility regarding the disposal of packaging materials.
Hence, the correct answer is Option (2)."
""",
    "4S": """"4 statement type
answer key - {answer_key}
topics - 
{topics}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
create 5 - 4 statement type questions - - very ugc net home science type, and very analytical. arrange the options such that the answer key is true. very very long and better explanation and explain all major keywords in 1 setence eac and dont type anything like topic or intro etc. remember to add the hence line at the end - important.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. just what i asked. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens - format -

--Question Starting--
1. Identify the key roles of packaging in the modern socio-scientific discipline from the following list:
I. Protecting against biological and chemical damages
II. Increasing shelf-life and availability
III. Disposal without environmental responsibility
IV. Marketing and advertising tool
Choose the correct answer from the options given below:
(1) I, II, III & IV Only
(2) I, II, IV Only
(3) I, III, IV Only
(4) II, III, IV Only
Answer Key: (2)
Solution:
Statement I is correct. Packaging plays a critical role in protecting products against biological, chemical, and distribution damages.
Statement II is correct. One of the major functions of packaging is to increase the shelf-life of products and ensure their availability for a longer time.
Statement IV is correct. Packaging also serves as a marketing and advertising tool, contributing to product image through design and labelling.
Statement III is incorrect because packaging emphasizes environmental responsibility regarding the disposal of packaging materials.
Hence, the correct answer is Option (2)."
""",
    "5S": """5 statement type
answer key - {answer_key}
topics - 
{topics}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
create 5 - 5 statement type questions - - very ugc net home science type, and very analytical. arrange the options such that the answer key is true. very very long and better explanation and explain all major keywords in 1 setence eac and dont type anything like topic or intro etc. remember to add the hence line at the end - important.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. just what i asked. 
when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens 
- format -

--Question Starting--
1. Identify the key roles of packaging in the modern socio-scientific discipline from the following list:
I. Protecting against biological and chemical damages
II. Increasing shelf-life and availability
III. Disposal without environmental responsibility
IV. Marketing and advertising tool
V. Convenience in handling and storage
Choose the correct answer from the options given below:
(1) I, II, III & IV Only
(2) I, II, IV & V Only
(3) I, III, IV & V Only
(4) II, III, IV & V Only
Answer Key: (2)
Solution:
Statement I is correct. Packaging plays a critical role in protecting products against biological, chemical, and distribution damages.
Statement II is correct. One of the major functions of packaging is to increase the shelf-life of products and ensure their availability for a longer time.
Statement IV is correct. Packaging also serves as a marketing and advertising tool, contributing to product image through design and labelling.
Statement V is correct. Providing convenience in handling, storage, and distribution is a key function of packaging.
Statement III is incorrect because packaging emphasizes environmental responsibility regarding the disposal of packaging materials.
Hence, the correct answer is Option (2).""",
    "SL": """ single liner
topic - 
{topics}
 arrange the option such that the answer key is - {answer_key}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
create 5 single liner type questions like this -  very analytical, very ugc net, home science. remember to add the hence line at the end - important. a lot longer and better explanation and explain all major keywords and dont type anything like topic name or intro etc.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. just what i asked. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens and use this VERY exact format - format - 

--Question Starting--
1. Which raising agent releasing both carbon dioxide and ammonia without leaving any residue?
(1) Sodium Bicarbonate
(2) Potassium Carbonate
(3) Ammonium Bicarbonate
(4) Calcium Phosphate
Answer Key: (3)
Solution:
Option (3) is correct. Ammonium bicarbonate is particularly valued because it decomposes upon heating at around 60°C, releasing carbon dioxide and ammonia and leaving no residue in the baked product. This is suitable for products like cookies, crackers, and cream puffs.
Option (1) is incorrect. Sodium bicarbonate releases carbon dioxide.
Option (2) is incorrect. Potassium carbonate requires an acid to release carbon dioxide and is less convenient to use. It doesn't release ammonia.
 Option (4) is incorrect. Calcium phosphate is a slow-acting acid component in baking powders but does not release gases.
Hence, the correct answer is Option (3).""",
    "AR": """AR
topics - 
{topics}
answer keys - {answer_key}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
arrange the options such that the answer key is true. create 5 assertion reasoning type questions like this - very ugc net type home science, and very analytical.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. a lot longer and better explanation and explain all major keywords in 1 setence each and dont type anything like topic name or intro etc. just what i asked. remember to add the hence line at the end - important. make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens, and use this VERY EXACT format  - format -

--Question Starting--
1. Given below are two statements, one is labelled as Assertion (A) and the other is labelled as Reason (R).
Assertion (A): Dairy products and other liquids have a longer shelf life thanks to High Temperature Short Time (HTST) pasteurization.
Reason (R): HTST pasteurization heats the product to a high temperature for a short duration and rapidly cools it to inactivate microorganisms.
In light of the above statements, choose the correct option:
(1) A is false but R is true.
(2) A is true but R is false.
(3) Both A and R are true, and R is the correct explanation of A.
(4) Both A and R are true, and R is not the correct explanation of A.
Answer Key: (3)
Solution:
Assertion (A) is true. After short heating a liquid (72°C–76°C for 15–20 seconds), high temperature short time (HTST) pasteurization rapidly cools a liquid to kill dangerous bacteria. This procedure greatly increases shelf life while maintaining product quality.
Reason (R) is true and is the correct explanation of the Assertion (A). The Reason accurately describes the mechanism through which HTST achieves this result short-term high-temperature exposure followed by rapid cooling to kill microbes and minimize product degradation. Thus, both the Assertion and Reason are true, and the Reason correctly explains the Assertion.
Hence, the correct answer is Option (3).""",
"CS": """ case study
topic - 
{topics}
arrange the questions such that the answer key is - {answer_key}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
5 more case study type questions like this - a bit harder, but mostly very very analytical. very ugc net home science type. remember to add the hence line at the end - important. explain all major keywords in 1 setence each. longer and better explanation and dont type anything like topic or intro etc. just what i asked.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. 
when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens and use this exact format - format -

--Question Starting--
1. A public service campaign utilizes television commercials, social media, and community health workers to disseminate information about the importance of vaccination for children and to address misinformation about vaccine safety. This initiative aims to improve child health outcomes and reduce the prevalence of preventable diseases.

According to the principles of development communication, which critical societal issue is this campaign primarily addressing?
(1) Population growth
(2) Health disparities
(3) Human rights violations
(4) Rural and tribal development
Answer Key: (2) 
Solution:
Option (2) is correct: The public service campaign focuses on disseminating crucial health information regarding childhood vaccinations and countering misinformation. The primary goal is to improve child health outcomes and reduce the occurrence of preventable diseases. This directly aligns with the aims of development communication in addressing health disparities by promoting health awareness, ensuring access to vital health knowledge, and ultimately working towards equitable health outcomes for children.
Option (1) is incorrect:  The population growth, is not the central focus of a vaccination campaign, although child health can indirectly influence population dynamics over time.
Option (3) is incorrect: The human rights violations, while important, is not the primary issue being tackled by a vaccination campaign. Access to healthcare can be considered a human right, but the campaign's direct focus is on health and disease prevention. 
Option (4) is incorrect: The rural and tribal development, while these communities might be specific targets for vaccination efforts due to potential disparities in access, the overarching societal issue being addressed by a widespread public service campaign on vaccination is broader than just these specific populations. The campaign aims to improve child health across all segments of society.
Hence, the correct answer is Option (2).""",
"CG":"""chronology
topics - 
{topics}
answer keys - {answer_key}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. 
arrange the options such that the answer key is true. create 5 chronology type questions like this - very ugc net type home science, and very analytical. a lot longer and better explanation and explain all major keywords in 1 setence each and dont type anything like topic name or intro etc.  just what i asked. remember to add the hence line at the end - important.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens and use this VERY exact format -

--Question Starting--
1. What is the correct physiological sequence of events involved in the absorption and regulation of sodium within the human body?
I. Sodium Movement via Na⁺/K⁺ Pump
II. Co-transport with Nutrients  
III. Reabsorption by Kidneys
IV. Absorption Driven by Bulk Flow
V. Hormonal Control and Excretion 
Choose the correct answer from the options given below:
(1) I, III, II, V, IV
(2) II, I, IV, III, V 
(3) II, I, III, IV, V
(4) I, II, III, V, IV
Answer Key: (2)
Solution:

Statement II - The initial site of sodium absorption and control is the small intestine. The sodium is absorbed through co-transport processes, with glucose or amino acids, particularly in the duodenum and jejunum.
Statement I - The Na+/K+-ATPase pump actively transports sodium into the bloodstream once it enters intestinal cells, preserving the concentration gradient necessary for further absorption.
Statement IV - The osmotic movement of fluids known as bulk flow play an additional role in sodium absorption by the body.
Statement III - Sodium regulation through the kidney occurs when these organs take up filtered salt following the absorption process.
Statement V - Aldosterone regulates how much sodium the body either keeps or releases depending on its needs thus supporting both fluid stability and proper functions of neurons and muscles.
Hence, the correct answer is Option (2).""",
"FU":"""fill blanks 
topic - 
{topics}

answer key - {answer_key}
difficulty - super hard - each question should be distinct and dont follow the same kind of pattern for each question. subject - ugc net home science
create 5 fill in the blanks type questions like this - as hard as you can make them, and very very analytical. and unique. a lot longer and better explanation and explain all major keywords in 1 setence each and dont type anything like topic name or intro etc. just what i asked. remember to add the hence line at the end - important.  Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions so please give appropriately tough questions
make sure you create exactly 5 questions, one from each topic and make sure to start every question with "--Question Starting--", this is extremely important, make sure that happens and use this VERY exact format  - format - 
 
--Question Starting--
1. Quality Assurance emphasizes ________ defects rather than just detecting them.
(1) Ignoring
(2) Documenting
(3) Preventing
(4) Highlighting
Answer Key: (3)
Solution:
Option (3) is correct. Quality Assurance (QA) focuses on building quality into the process itself to ensure that defects are avoided from the beginning.
Option (1) is incorrect. QA never ignores potential defects; it actively works to eliminate them.
Option (2) is incorrect. Documenting refers to recording information. It does not address the goal - prevention of QA.
Option (4) is incorrect. Highlighting involves pointing out defects after they occur, which is more aligned with Quality Control activities.
Thus, the correct answer is Option (3)."""
}