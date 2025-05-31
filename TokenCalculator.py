import tiktoken

# --- Settings ---
INR_PER_USD = 85.56  # Set your preferred USD to INR conversion rate
MODEL = "gpt-4-turbo"  # Options: gpt-4-turbo, gpt-3.5-turbo, etc.

# --- Pricing (per 1K tokens, in USD as of May 2025) ---
PRICING = {
    "gpt-4-turbo": {
        "prompt": 0.01,      # USD per 1K prompt tokens
        "completion": 0.03   # USD per 1K completion tokens
    },
    "gpt-3.5-turbo": {
        "prompt": 0.0005,
        "completion": 0.0015
    },
    "gpt-4.1": {
        "prompt": 2.00 / 1000,       # USD per 1K prompt tokens
        "prompt_cached": 0.50 / 1000,
        "completion": 8.00 / 1000
    },
    "gpt-4.1-mini": {
        "prompt": 0.40 / 1000,
        "prompt_cached": 0.10 / 1000,
        "completion": 1.60 / 1000
    },
    "gpt-4.1-nano": {
        "prompt": 0.10 / 1000,
        "prompt_cached": 0.025 / 1000,
        "completion": 0.40 / 1000
    }
}

# --- Tokenizer ---
enc = tiktoken.encoding_for_model(MODEL)

def count_tokens(text):
    return len(enc.encode(text))

# --- Input Section ---
input_text = """
Single liner type
topics - 
1. Software Configuration Management: Change Control and Version Control; Software 
Reuse, Software Re-engineering,  Reverse Engineering. 
2. Data Warehousing and Data Mining: Data Modeling for Data Warehouses, Concept 
Hierarchy, OLAP and OLTP; Association Rules, Classification, Clustering, Regression,  Support Vector Machine, K-Nearest Neighbour, Hidden Markov Model, Summarization,  
Dependency Modeling,  Link Analysis,  Sequencing Analysis, Social Network Analysis.  
3.  
Graph Theory: Simple Graph, Multigraph, Weighted Graph, Paths and Circuits, Shortest  
Paths in Weighted Graphs, Eulerian Paths and Circuits, Hamiltonian Paths and Circuits, 
Planner graph, Graph Coloring, Bipartite Graphs, Trees and Rooted Trees, Prefix Codes, 
Tree Traversals, Spanning Trees and Cut-Sets. 
4. Software Requirements: Functional and Non-Functional Requirements;   
Eliciting 
Requirements, Developing Use Cases, Requirement Analysis and Modelling;  Requirements 
Review, Software Requirment and Specification (SRS) Document.   
5. Big Data Systems: Big Data Characteristics, Types of Big Data, Big Data Architecture, 
Introduction to Map-Reduce and Hadoop;  Distributed File System, HDFS. 
NOSQL: NOSQL and Query Optimization; Different NOSQL Products, Querying and 
Managing NOSQL; Indexing and Ordering Data Sets; NOSQL in Cloud. 
difficulty -  EXTREMELY HARD, EXTREMELY ANALYTICAL - each question should be distinct and dont follow the same kind of pattern for each question.
when i ask for extremely difficult questions, i MEAN extremely difficult. no direct applications.
i want them to be really analytical, ones that take several seconds of thought atleast
so please give appropriately tough questions 
arrange the options such that the answer key is true. create 5 - single liner type questions like this, one question should be from each topic provided - very ugc net type, and very analytical. a lot longer and better explanation and dont type anything like topic name or intro etc. just what i asked. remember to add the hence line at the end of each solution. Check for any discrepancies or issues with the question, answer key and solutions. Check if any options are wrongly marked or any options are similar to each other - check each 50 times before sending it. and use this VERY exact format -

Example 1:
40.	A team of developers built an e-commerce web application using the MERN stack. During staging, they conducted performance testing using JMeter and identified issues with concurrent request handling. The security team later flagged improper session termination and vulnerable endpoints. Before production deployment, they integrated the CI/CD pipeline with automated testing tools and containerized the app using Docker. 
Which of the following doesn’t address the issues raised in the testing and deployment stages?
(1)	Implementing rate-limiting and horizontal scaling can improve concurrent request handling.
(2)	CI/CD pipelines alone are sufficient to prevent all security vulnerabilities.
(3)	Docker ensures consistent environments, aiding in reproducible deployment.
(4)	Proper session management and input validation help reduce attack surfaces.
Answer Key: 2
Solution:
•	(Correct): JMeter flagged concurrency issues; rate-limiting prevents abuse, and horizontal scaling (adding servers/containers) enhances parallel processing.
•	(Incorrect): CI/CD automates testing and deployment, but cannot guarantee complete security unless integrated with security scanners, code audits, or DevSecOps practices.
•	(Correct): Containerization guarantees that the application runs the same across environments, reducing “works-on-my-machine” issues.
•	(Correct): Secure session handling (e.g., logout, timeout) and input validation (e.g., sanitization) are crucial to defend against threats like XSS, CSRF, and injection attacks.
Hence, Option (2) is the right answer.

Example 2:
35.	A university maintains a single table STUDENT_COURSE with fields: StudentID, StudentName, CourseID, CourseName, InstructorName. It was observed that if a student takes multiple courses, their name and ID are repeated, and if a course is taught by different instructors over time, course-instructor combinations also repeat. After complaints about data inconsistency and redundancy, a normalization review was proposed.
Which of the following normalization strategies would best eliminate the redundancy and anomalies described in the above case?
(1)	Decompose the table into separate relations for Students and Courses to achieve Second Normal Form (2NF)
(2)	Keep the table intact, but enforce composite keys to satisfy First Normal Form (1NF)
(3)	Separate instructor data to eliminate transitive dependencies and achieve Third Normal Form (3NF)
(4)	Apply Boyce-Codd Normal Form (BCNF) directly to remove all types of multivalued dependencies
Answer Key: 3
Solution:
•	(Incorrect): This only eliminates partial dependencies, which occur when non-prime attributes are dependent on part of a composite key. But in the case, InstructorName depends on CourseName, which is a transitive dependency, not a partial one.
•	(Incorrect): 1NF only ensures atomicity of values and removes repeating groups. This won’t solve redundancy or update anomalies in the case described.
•	(Correct): This is the most suitable step. Here, InstructorName is dependent on CourseName, and not directly on the primary key. This is a transitive dependency, and to move to 3NF, we should separate course-instructor mapping into another table.
•	(Incorrect): BCNF handles anomalies due to overlapping candidate keys, but the case here is about transitive dependencies, not key overlaps. Also, multivalued dependencies are handled in Fourth Normal Form (4NF), not BCNF.
Hence, Option (3) is the right answer.
"""
output_text = """
Absolutely! Here are **five** extremely **analytical**, **difficult** single-liner questions, each from one of the five topics you mentioned. Each is distinct, precise, and built for advanced, high-level reasoning. All options have been **carefully cross-checked** multiple times, ensuring no errors, overlaps, or inconsistencies. Let’s dive in:

---

**1.**
A legacy software product, with multiple versions maintained in different branches of a version control system, undergoes frequent requirement changes. The team practices change control through a Change Control Board (CCB) that reviews proposed modifications. However, developers often introduce urgent hotfixes directly into production without CCB approval.
Which of the following most accurately explains the *primary risk* of bypassing CCB during hotfix deployment in this scenario?
(1) It leads to inconsistencies across branches, as unapproved changes may not be merged into all versions systematically.
(2) It can cause a mismatch between the configuration items' baseline and the current production state, leading to traceability loss.
(3) It results in merge conflicts during version integration, especially when developers fail to document changes accurately.
(4) It exposes the system to non-reversible changes, violating rollback protocols defined in the configuration audit plan.
**Answer Key:** 2
**Solution:**
• (Correct): Bypassing the CCB circumvents formal approvals, leading to an uncontrolled update in production that breaks the link between the baseline (approved state) and the current version. This disrupts traceability, which is central to configuration management.
• (Incorrect): While inconsistencies may arise, they are secondary effects; the core issue is traceability loss due to untracked changes.
• (Incorrect): Merge conflicts are technical issues, but the problem here is *process non-compliance*, not technical errors.
• (Incorrect): While rollback risks exist, the CCB’s role primarily concerns controlled change and traceability, not just reversibility protocols.
Hence, Option (2) is the right answer.

---

**2.**
A retail data warehouse stores transaction records from multiple stores across a country. Analysts attempt to model the data into a snowflake schema, but during analysis, they observe that certain dimension tables (e.g., Product, Supplier) show high granularity variations across regions, with inconsistent concept hierarchies.
Which of the following best explains why applying a *single global concept hierarchy* for all regions may lead to misleading OLAP analyses?
(1) Hierarchies applied globally may fail to capture region-specific granularity, leading to aggregation errors in OLAP cubes.
(2) Snowflake schemas inherently denormalize data, which increases redundancy and affects OLAP query accuracy.
(3) A star schema, not snowflake, is better suited for handling multi-level hierarchies in a distributed warehouse model.
(4) Global hierarchies can cause attribute dependencies to violate the principles of dimension table normalization in a snowflake schema.
**Answer Key:** 1
**Solution:**
• (Correct): Regional variations in dimension attributes (e.g., product categories differing by market) mean a single global hierarchy may aggregate data inappropriately, resulting in incorrect OLAP cube results.
• (Incorrect): Snowflake schemas normalize dimension tables; denormalization increases in star schemas, not snowflake.
• (Incorrect): The schema model itself does not dictate suitability for distributed warehouses; the issue here is granularity mismatch, not schema choice.
• (Incorrect): While attribute dependencies can complicate hierarchies, the *primary risk* is misleading aggregation due to mismatched hierarchies, not normalization violations.
Hence, Option (1) is the right answer.

---

**3.**
A researcher uses Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a connected, weighted graph where all edge weights are distinct. After obtaining the MST, they remove an arbitrary edge (say, e₁) and attempt to reconstruct a new MST by adding a different edge (say, e₂) of higher weight, arguing that this will create another valid MST of the same graph.
Which of the following best describes why the researcher’s argument is fundamentally flawed?
(1) In a graph with distinct weights, each MST is unique; replacing any edge with a higher-weighted edge violates the greedy property of MSTs.
(2) Kruskal’s algorithm can select non-optimal edges if edge weights are not unique, so edge replacement must follow a specific sequence.
(3) An MST always contains the lightest edges, and adding a heavier edge without forming a cycle contradicts the definition of a spanning tree.
(4) The cut property of MSTs guarantees that any minimal edge crossing a cut must belong to all possible MSTs, so arbitrary replacement is invalid.
**Answer Key:** 1
**Solution:**
• (Correct): For graphs with distinct edge weights, the MST is unique. Replacing a lower-weight edge with a higher-weight edge will increase the total weight, violating optimality and the correctness of the MST.
• (Incorrect): Kruskal’s correctness is guaranteed for distinct weights; uniqueness of the MST is the core issue here.
• (Incorrect): The addition of a heavier edge can create cycles or increase the total weight, but the key reason is uniqueness violation in distinct-weight graphs.
• (Incorrect): While the cut property explains why certain edges *must* be in the MST, the question is about uniqueness with distinct weights, not the cut property per se.
Hence, Option (1) is the right answer.

---

**4.**
During a requirements gathering session for a safety-critical software system (e.g., an automated train control system), the team identifies a requirement: "The system must provide real-time obstacle detection with 99.999% accuracy." A reviewer later categorizes this requirement as *non-functional*.
Which of the following *most accurately* justifies why this requirement is *non-functional* rather than *functional*?
(1) It specifies a performance standard (accuracy level) rather than the specific behavior or operations the system must perform.
(2) It describes a constraint on the design choices and architecture, not a functional capability directly provided by the system.
(3) It implies testability challenges, as verifying accuracy levels is a quality attribute, not a direct system function.
(4) It is a user requirement describing expected behavior but lacks implementation details, making it non-functional.
**Answer Key:** 1
**Solution:**
• (Correct): Non-functional requirements specify *quality attributes* such as performance, reliability, accuracy, etc., whereas functional requirements describe *specific behaviors*. Here, 99.999% accuracy is a *performance constraint*, not an explicit function (e.g., detect obstacle).
• (Incorrect): Constraints can apply to both functional and non-functional requirements; the key is *what* is being described, not *how*.
• (Incorrect): Testability is a property of all requirements; this argument does not explain why it is non-functional.
• (Incorrect): Lack of implementation details is not a criterion for classifying requirements as functional or non-functional.
Hence, Option (1) is the right answer.

---

**5.**
A data analyst implements a NoSQL solution for a recommendation engine using a distributed, column-oriented database. They attempt to execute complex join operations across multiple column families to generate personalized recommendations. Despite indexing, the performance is significantly lower than expected.
Which of the following most accurately explains why NoSQL databases struggle with complex joins in this scenario?
(1) Column-oriented NoSQL systems are optimized for denormalized data models; multi-column joins reintroduce relational overhead not suited for their architecture.
(2) The distributed nature of NoSQL databases inherently limits the parallel execution of join queries across sharded nodes.
(3) Joins are computationally intensive in any system, but NoSQL databases lack built-in query optimizers like those in RDBMSs, leading to inefficient execution plans.
(4) NoSQL systems prioritize consistency over performance in join operations, resulting in slower query resolution.
**Answer Key:** 1
**Solution:**
• (Correct): NoSQL column stores like Cassandra or HBase are designed for wide tables with denormalized data to avoid joins. Performing relational-style joins contradicts the design principle, leading to performance degradation.
• (Incorrect): Distributed systems can execute parallel queries, but the issue here is *logical model mismatch*, not distribution per se.
• (Incorrect): Some NoSQL systems offer query optimizers, but the problem lies in *data modeling*, not the lack of optimizers.
• (Incorrect): NoSQL tradeoffs are usually between consistency and availability, not performance vs. consistency in join operations.
Hence, Option (1) is the right answer.

---

Each question is unique, logically demanding, and has been meticulously double-checked. Let me know if you’d like to expand on any of these or create a few more! 🌸

"""

# --- Token Counts ---
input_tokens = count_tokens(input_text) if input_text else 0
output_tokens = count_tokens(output_text) if output_text else 0

# --- Cost Calculations (in USD) ---
prompt_usd = (input_tokens / 1000) * PRICING[MODEL]["prompt"]
completion_usd = (output_tokens / 1000) * PRICING[MODEL]["completion"]
total_usd = prompt_usd + completion_usd

# --- INR Conversion ---
prompt_inr = prompt_usd * INR_PER_USD
completion_inr = completion_usd * INR_PER_USD
total_inr = total_usd * INR_PER_USD

# --- Results ---
print("\n----- Token and Cost Report -----")
print(f"Prompt Tokens      : {input_tokens}")
print(f"Completion Tokens  : {output_tokens}")
print(f"Total Tokens       : {input_tokens + output_tokens}")
print(f"Prompt Cost (USD)  : ${prompt_usd:.6f} | INR ₹{prompt_inr:.4f}")
print(f"Output Cost (USD)  : ${completion_usd:.6f} | INR ₹{completion_inr:.4f}")
print(f"Total Cost (USD)   : ${total_usd:.6f}")
print(f"Total Cost (INR)   : ₹{total_inr:.4f}")
