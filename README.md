# Single-Cell RNA Sequencing (scRNA-seq) and Cancer Evolution

---

## **Introduction**

Cancer is a disease marked by genomic instability that advances through the birth of diverse clones, their subsequent selection and adaptive changes—processes that echo Darwinian evolution (Greaves & Maley, 2012). Although bulk next-generation sequencing of tumor specimens has uncovered many driver mutations and repeatedly altered pathways (Hua et al., 2013; Raphael et al, 2014), this strategy essentially averages the signal from millions of cells. As a result, rare subpopulations—those that might later dominate growth or fuel drug resistance—can be hidden from view (McGranahan & Swanton, 2017; Li et al., 2021; Erfanian et al., 2023).

Single-cell RNA sequencing (scRNA-seq) overcomes this limitation by profiling the entire transcriptome of each individual cell. In doing so, it lays bare cellular heterogeneity, maps lineage relationships, and reveals how plastic cell states can be—all at a resolution that was previously unattainable (Tang et al., 2009; Luecken & Theis, 2019). When researchers interrogate anywhere from a few thousand to several million tumor-derived cells (Chockalingam et al., 2025), they can reconstruct the evolutionary paths that tumors follow (Liu et al., 2024; Hodzic et al., 2020), link specific genotypes to phenotypic outputs (Poirion et al., 2018; Penter et al., 2024), and study the tumor microenvironment (TME) within a single, integrated analytical framework (Liu et al., 2023).  

These advances have reshaped our mental picture of cancer: rather than static lumps, tumors are now seen as dynamic ecosystems populated by distinct cellular “species” that compete, cooperate, and adapt under selective pressures (Marjanovic et al., 2020; Maley et al., 2017).

In this review we bring together the most recent evidence showing how scRNA-seq is redefining our understanding of cancer evolution. We concentrate on three interrelated themes:  
(i) the technical foundations that make the method possible,  
(ii) the fresh insights it provides into intratumoral heterogeneity, and  
(iii) what it reveals about mechanisms of therapy resistance and their translational implications (Lee et al., 2014; Mossner et al., 2021; Otsuji et al., 2024; Zhang et al., 2022).

---

#### **References**

Chockalingam, S. P., et al. (2025). *SCEMENT: Scalable and memory efficient integration of large-scale single-cell RNA-seq data.* **Bioinformatics**, 41(2), btaf057. https://doi.org/10.1093/bioinformatics/btaf057  
Erfanian, N., et al. (2023). *Deep learning applications in single-cell genomics and transcriptomics data analysis.* **Biomedicine & Pharmacotherapy**, 165, 115077. https://doi.org/10.1016/j.biopha.2023.115077  
Greaves, M., & Maley, C. C. (2012). *Clonal evolution in cancer.* **Nature**, 481(7381), 306-313. https://doi.org/10.1038/nature10762  
Hodzic, E., et al. (2020). *Identification of conserved evolutionary trajectories in tumors.* **Bioinformatics**, 36(Supplement_1), i427-i435. https://doi.org/10.1093/bioinformatics/btaa453  
Hua, X., et al. (2013). *DrGaP: A powerful tool for identifying driver genes and pathways in cancer sequencing studies.* **American Journal of Human Genetics**, 93(3), 439-451. https://doi.org/10.1016/j.ajhg.2013.07.003  
Li, X., et al. (2021). *From bulk, single-cell to spatial RNA sequencing.* **International Journal of Oral Science**, 13, 36. https://doi.org/10.1038/s41368-021-00146-0  
Liu, W., et al. (2023). *Characterizing the tumor microenvironment at the single-cell level.* **Bone Research**, 11(1), 6. https://doi.org/10.1038/s41413-022-00237-6  
Liu, Z. L., et al. (2024). *Single cell deciphering of progression trajectories of head and neck squamous cell carcinoma.* **Nature Communications**, 15, 2449. https://doi.org/10.1038/s41467-024-46912-6  
Luecken, M. D., & Theis, F. J. (2019). *Current best practices in single-cell RNA-seq analysis: a tutorial.* **Molecular Systems Biology**, 15(6), e8746. https://doi.org/10.15252/msb.20188746  
Lee, M. C., Lopez-Diaz, F. J., Khan, S. Y., et al. (2014). *Single-cell analyses of transcriptional heterogeneity during drug tolerance transition in cancer cells by RNA sequencing.* **PNAS**, 111(44), E4726-E4735. https://doi.org/10.1073/pnas.1404656111  
Maley, C. C., et al. (2017). *Classifying the evolutionary and ecological features of neoplasms.* **Nature Reviews Cancer**, 17(10), 605-619. https://doi.org/10.1038/nrc.2017.69  
Marjanovic, N. D., Hofree, M., Chan, J. E., et al. (2020). *Emergence of a high-plasticity cell state during lung cancer evolution.* **Cancer Cell**, 38(2), 229-246.e13. https://doi.org/10.1016/j.ccell.2020.06.012  
McGranahan, N., & Swanton, C. (2017). *Clonal heterogeneity and tumor evolution: Past, present, and the future.* **Cell**, 168(4), 613-628. https://doi.org/10.1016/j.cell.2017.01.018  
Mossner, M., et al. (2021). *The role of single-cell sequencing in studying tumour evolution.* **Briefings in Functional Genomics**, 20(4), 197-206. https://doi.org/10.1093/bfgp/elab014  
Otsuji, K., et al. (2024). *Serial single-cell RNA sequencing unveils drug resistance evolution in metastatic melanoma.* **npj Precision Oncology**, 8, 213. https://doi.org/10.1038/s41698-024-00723-6  
Penter, L., et al. (2024). *Integrative genotyping of cancer and immune phenotypes by long-read sequencing.* **Nature Communications**, 15, 44. https://doi.org/10.1038/s41467-023-44137-7  
Poirion, O., et al. (2018). *Using single nucleotide variations in single-cell RNA-seq to study subpopulation structure and genotype-phenotype linkage.* **Nature Communications**, 9, 4892. https://doi.org/10.1038/s41467-018-07170-5  
Raphael, B. J., et al. (2014). *Identifying driver mutations in sequenced cancer genomes: Computational approaches to enable precision medicine.* **Genome Medicine**, 6, 5. https://doi.org/10.1186/gm524  
Tang, F., Barbacioru, C., Wang, Y., Nordman, E., Lee, C., Xu, N., Wang, X., Bodeau, J., Tuch, B. B., Siddiqui, A., Lao, K., & Surani, M. A. (2009). *mRNA-Seq whole-transcriptome analysis of a single cell.* **Nature Methods**, 6, 377–382.  

---

## **Inside the Process: Workflow of scRNA-Seq**

Single-cell RNA follows a stepwise process which involves cell isolation by dissociating tissues into single cells, conversion of unstable RNA into complementary DNA (cDNA), amplification of cDNA, and sequencing it using high-throughput technology to determine the order of nucleotides (A, U/T, C, G).  
The resulting data then undergo computational processing, alignment, and downstream analysis using bioinformatics tools for visualization and interpretation (Tang et al., 2009).

---

## **Application of scRNA-seq in Cancer: Insights into Tumor Diversity**

scRNA-seq has emerged as a powerful and versatile tool for both basic and clinical research and has been proven to be an invaluable technology in cancer biology (Aran et al., 2015).  
Before the advent of scRNA-seq, tumors were largely viewed as simple clusters of rapidly dividing cells. Today, we know that tumors are far more complex—they contain not only cancerous cells but a mix of other cell types, signaling molecules, and nutrients that together create a dynamic environment influencing both tumor growth and suppression.  

This complexity, known as **tumor heterogeneity**, is one of the main reasons scRNA-seq has become a significant approach for studying cancer evolution (Grivennikov et al., 2010).  

From a computational viewpoint, large-scale initiatives such as **The Cancer Genome Atlas (TCGA)** (Weinstein et al., 2013) have used RNA sequencing to analyze thousands of tumor samples, helping scientists uncover valuable insights into cancer subtypes, biomarkers, and potential drug targets. However, while bulk RNA-seq has provided broad information about average gene expression across tumors, it masks the important variations between individual cells.  

scRNA-seq overcomes this limitation by profiling gene expression at the single-cell level, revealing the hidden genetic diversity and evolutionary patterns that shape cancer behavior.  

In cancer biology, a **clone** refers to a group of tumor cells that originate from a single parent and share the same genetic makeup. As cancer develops, these clones accumulate new mutations, giving rise to **subclones** with slightly different characteristics. Using scRNA-seq, researchers can identify these subclones and reconstruct their evolutionary relationships based on gene expression and mutation profiles.  

This reveals how certain clones gain survival advantages under selective pressures such as therapy, immune attack, or lack of oxygen—leading to branching evolutionary paths rather than a linear pattern of tumor growth (Aran, 2023).  

Beyond genetic mutations, scRNA-seq has shown that cancer cells exhibit **transcriptional plasticity**—they change their behavior without altering their DNA, helping them shift between dormant and active states (Patel et al., 2014).  

Additionally, scRNA-seq allows for the study of non-cancerous cells surrounding tumor cells, such as immune cells, fibroblasts, and endothelial cells, collectively known as the **Tumor Microenvironment (TME)**.  
By analyzing how these cells communicate through signaling molecules and cytokines, researchers can discover how tumors evade the immune system and promote inflammation.  

The single-cell perspective shows that cancer evolution is shaped not only by intrinsic genetic changes but also by constant interactions between tumor cells and their surrounding ecosystem (Ma et al., 2021).

---

#### **References**

1. Tang, F. et al. *mRNA-seq whole-transcriptome analysis of a single cell.* **Nature Methods.** 2009; 6, 377–382.  
2. Aran, D., Sirota, M., Butte, A. J. *Systematic pan-cancer analysis of tumour purity.* **Nature Communications.** 2015; 6:8971.  
3. Grivennikov, S. I., Greten, F. R., Karin, M. *Immunity, inflammation, and cancer.* **Cell.** 2010; 140:6883–99.  
4. Weinstein, J. N., Collisson, E. A., Mills, G. B., Shaw, K. M., Ozenberger, B. A., et al. *The Cancer Genome Atlas Pan-Cancer analysis project.* **Nature Genetics.** 2013; 45:101113–20.  
5. Aran, D. *Single-cell RNA sequencing for studying human cancers.* **Nature Reviews Cancer.** 2023; 23(4):239-258.  
6. Patel, A. P., et al. *Single-cell RNA-seq highlights intratumoral heterogeneity in primary glioblastoma.* **Science.** 2014; 344(6190):189-196.  
7. Ma, L., et al. *Tumor cell biodiversity drives microenvironment reprogramming in liver cancer.* **Cancer Cell.** 2021; 13(10):1294-1310.  

---

## **Application of scRNA-seq in Cancer: Uncovering Therapy Resistance and Clinical Implications**

One of the major clinical challenges in oncology is the emergence of **therapy resistance**, which frequently leads to disease relapse and poor patient outcomes. Traditional bulk sequencing approaches provide only an averaged signal across millions of cells, thereby masking the existence of rare resistant subpopulations that drive treatment failure.  

Single-cell RNA sequencing (scRNA-seq) has revolutionized our ability to dissect these complex dynamics by capturing transcriptional heterogeneity at single-cell resolution, allowing researchers to trace the origins and evolution of therapy-resistant clones (Zhang et al., 2025).

scRNA-seq studies have revealed that therapy resistance can emerge through multiple, coexisting mechanisms.  
- In some tumors, resistant cells pre-exist within the malignant population prior to treatment, representing a minor subclone that expands under therapeutic pressure—a striking example of **Darwinian selection** at the cellular level (Kunz et al., 2022).  
- In other cases, cancer cells display **transcriptional plasticity**, dynamically reprogramming their gene expression profiles in response to drug exposure—a process consistent with adaptive, **Lamarckian-like evolution**.  

For example, in melanoma, scRNA-seq identified pre-resistant subpopulations with neural crest–like signatures that survive MAPK inhibitor therapy and subsequently drive recurrence (Lin et al., 2024).  
Similarly, in **non-small cell lung cancer (NSCLC)**, single-cell profiling has uncovered diverse resistance trajectories following EGFR or immune checkpoint inhibitor treatments, including **epithelial-to-mesenchymal transition (EMT)** and **metabolic rewiring** (Zhai et al., 2022; Wang et al., 2024).

Beyond tumor-intrinsic mechanisms, scRNA-seq also highlights the contribution of the **tumor microenvironment (TME)** in therapy resistance.  
Immune and stromal cells can create protective niches that support resistant phenotypes. Remodeling of myeloid and fibroblast populations after chemotherapy, for instance, has been shown to promote a pro-survival microenvironment—emphasizing that resistance is often a **multicellular, ecosystem-level phenomenon** (Zhang et al., 2025).

These insights have profound clinical implications.  
By mapping resistant cell states before and after therapy, scRNA-seq enables the identification of **predictive biomarkers** and **novel therapeutic targets**.  
Integrating scRNA-seq with lineage tracing and spatial transcriptomics further reveals how resistant cells evolve *in situ*, providing a framework for the rational design of combination therapies aimed at preventing or delaying resistance.  

As single-cell technologies continue to mature, their incorporation into clinical workflows could enable **real-time monitoring** of tumor evolution and guide **adaptive, personalized treatment strategies.**

---

#### **References**

1. Kunz, M. et al. (2022). *Single-cell trajectories of melanoma cell resistance to targeted treatment.* **Cancer Biology & Medicine**, 19(11), 1581–1596. https://pubmed.ncbi.nlm.nih.gov/34591417  
2. Lin, X. et al. (2024). *Treatment resistance to melanoma therapeutics on a single cell level.* **Scientific Reports**, 14(1), 2312. https://pmc.ncbi.nlm.nih.gov/articles/PMC11413001  
3. Zhai, H. et al. (2022). *Molecular profiling of human non-small cell lung cancer by single-cell RNA-seq.* **Genome Medicine**, 14(1), 117. https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-022-01089-9  
4. Wang, Y. et al. (2024). *Single-cell RNA sequencing of baseline PBMCs predicts ICI efficacy in NSCLC patients.* **Frontiers in Immunology**, 15, 40404203. https://pubmed.ncbi.nlm.nih.gov/40404203  
5. Zhang, L. et al. (2025). *Application of single-cell and spatial omics in deciphering cellular hallmarks of cancer drug response and resistance.* **Journal of Hematology & Oncology**, 18(1), 1722. https://jhoonline.biomedcentral.com/articles/10.1186/s13045-025-01722-1  

---

## **Conclusion and Future Perspectives**

Single-cell RNA sequencing has fundamentally redefined our understanding of cancer. Once viewed as a homogenous mass of rapidly dividing cells, cancer is now recognized as a **dynamic and evolving ecosystem** composed of diverse cellular populations that adapt, interact, and compete under selective pressures.  

By capturing transcriptional heterogeneity at the single-cell level, scRNA-seq reveals the characteristics that drive disease progression and therapy resistance.

Although scRNA-seq continues to advance rapidly, it still faces several challenges such as high costs, uneven amplification, and the complexity of data interpretation. Addressing these limitations will require future improvements in sensitivity, throughput, and reproducibility—as well as integration with **multi-omics technologies** to provide a more comprehensive view of tumor biology.  

At the same time, continued progress in computational methods and machine learning analysis will be essential for managing the massive datasets generated and for revealing the full potential of scRNA-seq.  

All of these strategies reveal great potential not only in fundamental research but also in **environmental and clinical applications**, especially **personalized cancer treatment**.

---
