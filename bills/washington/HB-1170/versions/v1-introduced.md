1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

## ENGROSSED SECOND SUBSTITUTE HOUSE BILL 1170

## State of Washington

## 69th Legislature

2026 Regular Session

By House  Technology,  Economic  Development,  &amp;  Veterans  (originally sponsored  by  Representatives  Shavers,  Taylor,  Ryu,  Ramel,  Fosse, Wylie, Pollet, Ormsby, and Hill)

READ FIRST TIME 01/20/26.

AN ACT Relating to informing users when content is developed or modified by artificial intelligence; adding a new chapter to Title 19 RCW; and providing an effective date.

## BE IT ENACTED BY THE LEGISLATURE OF THE STATE OF WASHINGTON:

NEW SECTION. Sec. 1. The legislature finds that as generative artificial intelligence models become increasingly sophisticated, and the content created by such models proliferates across commonly used platforms, it can be difficult for the public to trust the accuracy, authenticity,  or  origin  of  information  accessed  on  the  internet. Recent technological advances allow providers of generative artificial intelligence systems to use watermarking and other technologies to label or detect content created using their proprietary  models.  By  ensuring  that  the  public  has  access  to reliable  provenance  data,  the  providers  of  generative  artificial intelligence systems can improve the public's ability to assess the accuracy  and  authenticity  of  synthetic  content,  thereby  helping  to reduce risks of misinformation.

NEW  SECTION. Sec.  2. The  definitions  in  this  section  apply throughout this chapter unless the context clearly requires otherwise.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

- (1)  "Artificial  intelligence"  means  the  use  of  machine  learning and  related  technologies  that  use  data  to  train  statistical  models for  the  purpose  of  enabling  computer  systems  to  perform  tasks normally  associated  with  human  intelligence  or  perception,  such  as computer  vision,  speech  or  natural  language  processing,  and  content
2. generation.
3. (2)(a) "Covered provider" means a person who:
4. (i)  Has  used,  or  intends  to  use,  a  quantity  of  computing  power greater  than  10^26  integer  or  floating-point  operations  to  train  a foundation model, including the computing power used for the original training  run  and  for  any  subsequent  fine  tuning,  reinforcement learning, or other material modifications made to a preceding foundation model;
5. (ii)  Uses  such  foundation  model  to  create,  code,  or  otherwise produce a generative artificial intelligence system that is publicly accessible  within  the  geographic  boundaries  of  the  state,  excluding generative  artificial  intelligence  systems  licensed  or  sold  for business-to-business purposes; and
6. (iii)  Collectively,  together  with  any  affiliates,  had  annual gross  revenues  in  excess  of  $500,000,000  in  the  preceding  calendar year.
7. (b)  "Covered  provider"  does  not  mean  public  entities  or  tribal nations.
- (3)  "Generative  artificial  intelligence"  means  an  artificial intelligence system that generates novel data or content based on a foundation model.
- (4) "Latent" means present but not manifest.
- (5) "Manifest" means easily perceived, understood, or recognized by a natural person.
- (6) "Metadata" means structural or descriptive information about data.
- (7) "Personal information" has the same meaning as defined in RCW 19.373.010.
- (8) "Personal provenance data" means provenance data that contains either of the following:
14. (a) Personal information; or
15. (b) Unique device, system, or service information that is reasonably capable of being associated with a particular user.
- (9)  "Provenance  data"  means  data  that  is  embedded  into  digital content or that is included in the digital content's metadata for the

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

- purpose  of  verifying  the  digital  content's  authenticity,  origin,  or history of modification.
- (10) "System provenance data" means provenance data that is not reasonably  capable  of  being  associated  with  a  particular  user  and that contains either of the following:
- (a) Information regarding the type of device, system, or service that was used to generate a piece of digital content; or
- (b) Information that helps a user assess authenticity.
- NEW  SECTION. Sec.  3. (1)  A  covered  provider  shall  make available  a  provenance  detection  tool  at  no  cost  to  the  user  that meets all of the following criteria:
- (a)  The  tool  allows  a  user  to  assess  whether  image,  video,  or audio  content,  or  content  that  is  any  combination  thereof,  was created  or  altered  by  the  covered  provider's  generative  artificial intelligence system;
- (b) The tool outputs any system provenance data that is detected in the content;
- (c)  The  tool's  results  are  publicly  accessible,  whether  by release  of  the  tool  directly  or  by  services  that  provide  access  to the  tool's  outputs,  and  a  covered  provider  may  impose  reasonable limitations  on  access  to  the  tool  to  prevent,  or  respond  to, demonstrable  risks  to  the  security  or  integrity  of  its  generative artificial intelligence system;
- (d) The tool allows a user to upload content or provide a uniform resource locator linking to online content; and
- (e)  Users  can  invoke  the  tool  without  visiting  the  covered provider's  internet  website,  for  instance,  through  an  application programming interface.
- (2) A covered provider shall collect user feedback related to the efficacy  of  the  covered  provider's  provenance  detection  tool  and consider  relevant  feedback  as  part  of  any  attempt  to  improve  the efficacy of the tool.
- (3) A covered provider may not do any of the following:
- (a)  Collect  or  retain  personal  information  from  users  of  the covered provider's provenance detection tool, except:
- (i)  A  covered  provider  may  collect  and  retain  the  contact information of a user who submits feedback pursuant to subsection (2) of this section if the user opts in to being contacted by the covered provider; and

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

- (ii) User information collected may only be used to evaluate and
- improve  the  efficacy  of  the  covered  provider's  provenance  detection tool;
- (b) Retain any content submitted to the provenance detection tool
- for longer than is necessary to comply with this section; or
- (c) Retain any personal provenance data from content submitted to
- the provenance detection tool by a user.
- (4) If a covered provider makes available a provenance detection tool  for  the  purpose  of  complying  with  another  applicable  law  or regulation, the provenance detection tool shall be deemed to satisfy the  requirements  established  in  this  section  if  such  provenance detection  tool  is  reasonably  similar  in  scope  and  effect  to  the provenance  detection  tool  that  would  otherwise  be  made  available
- pursuant to this section.

NEW  SECTION. Sec.  4. (1)  A  covered  provider  shall  offer  the user the option to include a manifest disclosure in image, video, or audio content, or content that is any combination thereof, created or altered by the covered provider's generative artificial intelligence system that meets all of the following criteria:

- (a) The disclosure identifies content as artificial intelligence-
- generated or artificial intelligence-modified content;
- (b)  The  disclosure  is  clear,  conspicuous,  appropriate  for  the medium of the content, and understandable to a reasonable person; and
- (c)  The  disclosure  is  difficult  to  remove,  to  the  extent  it  is technically feasible.
- (2)  A  covered  provider  shall  include  a  latent  disclosure  in artificial intelligence-generated image, video, or audio content, or content  that  is  any  combination  thereof,  created  by  the  covered provider's  generative  artificial  intelligence  system  that  meets  all of the following criteria:
- (a) To the extent it is technically feasible and reasonable, the disclosure conveys all of the following information, either directly or through a link to a permanent internet website:
- (i) The name of the covered provider;
- (ii)  The  name  and  version  number  of  the  generative  artificial intelligence system that created or altered the content;
- (iii)  The  time  and  date  that  the  disclosure  was  added  to  the generated or altered content;
- (iv) A unique identifier; and

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

- (v)  Personal  provenance  information  only  to  the  extent  that  a user has affirmatively chosen to add such information;
- (b)  The  disclosure  is  detectable  by  the  covered  provider's provenance detection tool;
- (c)  The  disclosure  is  consistent  with  widely  accepted  industry standards;
- (d) The disclosure is difficult to remove or recoverable, to the extent it is technically feasible.
- (3)(a)  If  a  covered  provider  licenses  its  generative  artificial intelligence  system  to  a  third  party,  the  covered  provider  shall require by contract that the licensee maintain the system's capability to include a disclosure required by subsection (2) of this section in content the system creates or alters.
- (b)  If  a  covered  provider  knows  that  a  third-party  licensee modified  a  licensed  generative  artificial  intelligence  system  such that  it  is  no  longer  capable  of  including  a  disclosure  required  by subsection  (2)  of  this  section  in  content  the  system  creates  or alters, the covered provider shall revoke the license within 96 hours of discovering the licensee's action.
- (c) A third-party licensee shall cease using a licensed generative  artificial  intelligence  system  after  the  license  for  the system  has  been  revoked  by  the  covered  provider  pursuant  to  (b)  of this subsection.
- (d) The provisions of this subsection do not apply to a license to a third party for internal business purposes, where such generative artificial intelligence system will not be made available by the third party to the general public.
- (4) A covered provider is not in violation of this chapter solely because  the  manifest  or  latent  disclosure  required  by  this  section was unintentionally removed, altered, or rendered unreadable, provided that the removal, alteration, or corruption occurred despite the  covered  provider's  use  of  commercially  reasonable,  industryaccepted  technical  and  organizational  measures  designed  to  preserve each disclosure.
- (5) A covered provider is not required to include disclosures in accordance  with  this  section  for  real-time  translation  of  text  or speech.

NEW  SECTION. Sec.  5. (1)  This  act  does  not  apply  to  any product,  service,  internet  website,  or  application  that  provides

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

exclusively video game or interactive experiences including, but not limited  to,  the  sale  of  goods  or  services  directly  to  consumers through  the  internet,  allowing  customers  to  browse,  select,  and

- purchase items virtually.
- (2) This act does not apply to systems used solely for upscaling, noise reduction, or compression.

NEW SECTION. Sec. 6. (1) Any waiver of the provisions of this chapter is contrary to public policy and is void and unenforceable.

- (2) The attorney general may bring an action in the name of the state,  or  as  parens  patriae  on  behalf  of  persons  residing  in  the state, to enforce this chapter. For actions brought by the attorney general  to  enforce  this  chapter,  the  legislature  finds  that  the practices covered by this chapter are matters vitally affecting the public interest for the purpose of applying the consumer protection act, chapter 19.86 RCW. For actions brought by the attorney general to enforce this chapter, a violation of this chapter is not reasonable in relation to the development and preservation of business and is an unfair or deceptive act in trade or commerce and an unfair method of competition for purposes of applying the consumer protection act, chapter 19.86 RCW.
- (3)  Only  the  attorney  general  can  bring  an  action  under  the consumer protection act, chapter 19.86 RCW, pursuant to this section.
3. NEW  SECTION. Sec.  7. Sections  1  through  6  of  this  act 23 constitute a new chapter in Title 19 RCW. 24
4. NEW SECTION. Sec. 8. This act takes effect January 1, 2028. 25

## --- END ---