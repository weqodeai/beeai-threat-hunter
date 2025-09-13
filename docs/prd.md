# Product Requirements Document (PRD)

## 1. ชื่อโปรเจกต์
AI Agents Team for SOC & Threat Hunting

## 2. แรงบันดาลใจและเป้าหมายโครงการ (Inspiration & Project Goal)
พัฒนา AI Agents Team เพื่อสนับสนุนงาน SOC (Security Operations Center) ในแต่ละวัน โดยเน้นการช่วยวิเคราะห์และจัดลำดับความสำคัญของเหตุการณ์ที่ควรจัดการก่อน, ค้นหาความสัมพันธ์ของเหตุการณ์แบบตรงจุด, และสามารถทำหน้าที่ Threat Hunter ในการช่วยเหลือองค์กรที่สงสัยว่าถูก Compromised โดยสามารถติดตั้ง Sensor เพื่อรวบรวมข้อมูลจากแหล่งต่างๆ เช่น Clickhouse, AD, DNS server และอื่นๆ ตามความเหมาะสม

## 3. ขอบเขตงาน (Scope)
- เชื่อมต่อและทำงานร่วมกับ MindsDB Agent เพื่อสืบค้นข้อมูลภัยคุกคามไซเบอร์จาก Clickhouse (Zeek, Suricata, Beelzebub, Shadowserver, Firewall, EDR)
- รองรับการเชื่อมต่อ Threat Intelligence ภายในและภายนอก (เป็นส่วนเสริม)
- ตรวจสอบ ปรับปรุง และ enrichment ข้อมูลที่ได้จาก MindsDB Agent
- มีระบบ Investigation Case Management สำหรับบันทึกและสืบค้นข้อมูลย้อนหลัง
- รองรับการเพิ่มแหล่งข้อมูลใหม่ เช่น AD, DNS server, หรือแหล่งข้อมูลอื่นที่เกี่ยวข้อง
- ใช้งานผ่าน BeeAI UI (ยังไม่พัฒนา Web-UI เฉพาะ)

## 4. กลุ่มเป้าหมาย (Target Users)
- SOC Analyst, Threat Hunter, Incident Response Team, Cybersecurity Engineer

## 5. ฟีเจอร์หลัก (Key Features)
1. **Integration กับ MindsDB Agent**
   - Query ข้อมูลภัยคุกคามจาก Clickhouse (Zeek, Suricata, Beelzebub, Shadowserver, Firewall, EDR)
   - รองรับการเพิ่มแหล่งข้อมูล เช่น AD, DNS server
   - รับและประมวลผลข้อมูลจาก MindsDB Agent
2. **Threat Intelligence Integration**
   - รองรับการเชื่อมต่อกับ Threat Intelligence ภายในและภายนอก (API/SDK)
3. **Result Validation & Enrichment**
   - ตรวจสอบความถูกต้องของผลลัพธ์
   - ปรับปรุง/เติมข้อมูล (Enrichment) เช่น IOC, TTP, Context
4. **Investigation Case Management**
   - สร้าง/บันทึก/ปรับปรุง/ค้นหาเคส Investigation
   - เก็บข้อมูลหลักฐาน, Timeline, Note, Status
5. **Prioritization & Correlation**
   - วิเคราะห์และจัดลำดับความสำคัญของเหตุการณ์ที่ต้องจัดการก่อน
   - ค้นหาความสัมพันธ์ของเหตุการณ์แบบตรงจุด (Event Correlation)
6. **Platform Integration**
   - ใช้งานผ่าน BeeAI Platform/Framework
   - รองรับการบริหารจัดการ Agent ผ่าน BeeAI
7. **Technology Stack**
   - Clickhouse, MindsDB, BeeAI Platform/Framework, Gel (EdgeDB เดิม) สำหรับ Case Management

## 6. ข้อกำหนดเทคโนโลยี (Technical Requirements)
- ใช้ Standard SDK ของแต่ละแพลตฟอร์มในการเชื่อมต่อและพัฒนา
- ระบบต้อง Clean, Professional, มี Code Comment ที่ดี
- ห้ามใช้ Emoji ในทุกส่วนของโครงการ (Code, Docs, Output)
- รองรับการขยายฟีเจอร์ Threat Intelligence และแหล่งข้อมูลใหม่ในอนาคต
- รองรับการใช้งานผ่าน BeeAI UI เป็นหลักในเฟสแรก

## 7. ข้อจำกัด (Constraints)
- ไม่พัฒนา Web-UI เฉพาะในเฟสแรก
- ระบบต้องสามารถเชื่อมต่อกับ Clickhouse และ MindsDB ที่ผู้ใช้เตรียมไว้
- Case Management ใช้ Gel (EdgeDB เดิม) เป็นหลัก

## 8. ข้อเสนอแนะเพิ่มเติม (Recommended Enhancements)
- เพิ่ม Agent เฉพาะทาง เช่น IOC Enrichment, Alert Correlation, Automated Playbook
- รองรับการ Integrate กับ SOAR หรือ SIEM ในอนาคต
- รองรับการ Export/Import ข้อมูล Investigation Case เป็นไฟล์มาตรฐาน (JSON, CSV)

## 9. ตัวอย่าง Workflow (High-level)
1. User สั่งงานผ่าน BeeAI UI → AI Agents Team รับโจทย์
2. Analyst Agent แปลงความต้องการเป็น Query/Task
3. Integration Agent เชื่อมต่อ MindsDB → Query ข้อมูลภัยคุกคาม
4. Validation/Enrichment Agent ตรวจสอบและเติมข้อมูล
5. Prioritization/Correlation Agent วิเคราะห์ความสำคัญและความสัมพันธ์ของเหตุการณ์
6. Case Management Agent สร้าง/อัปเดต Investigation Case ใน Gel
7. User ตรวจสอบผลลัพธ์และติดตามเคสผ่าน BeeAI UI

## 10. เอกสารอ้างอิง
- [BMAD-METHOD™ GitHub](https://github.com/bmad-code-org/BMAD-METHOD)
- [BeeAI Platform/Framework]
- [MindsDB Documentation]
- [Clickhouse Documentation]
- [Gel (EdgeDB) Documentation]

---

หมายเหตุ:
- PRD นี้ออกแบบให้สอดคล้องกับ BMAD-METHOD สามารถนำไปใช้ใน Agentic Planning ได้ทันที
- หากต้องการรายละเอียด Use Case, User Story, หรือ Diagram เพิ่มเติม แจ้งได้ทันที
