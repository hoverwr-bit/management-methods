# Sơ đồ các phương pháp quản trị (mã nguồn mở · có thể chỉnh sửa · tổng cộng 60 phương pháp)

**Ngôn ngữ / Language**：**Tiếng Việt** · [English](README.en.md) · [中文](README.md)

Tất cả sơ đồ đều được vẽ bằng cú pháp văn bản **Mermaid** (định dạng mã nguồn mở, [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) 82k+ stars).
Mọi công cụ hỗ trợ Mermaid đều có thể render trực tiếp thành biểu đồ:

- **File `index.html` trong thư mục này**: nhấp đúp để xem toàn bộ sơ đồ đã render trong trình duyệt (không cần cài đặt gì)
- **GitHub / Gitee**: tải lên trực tiếp, tự động render
- **VS Code**: cài plugin "Markdown Preview Mermaid Support"
- **Typora / Obsidian**: hỗ trợ sẵn

Chỉ cần sửa văn bản là chỉnh được sơ đồ, không cần phần mềm vẽ.

## Tra cứu theo kịch bản

| Việc bạn cần làm | Công cụ đề xuất |
|---|---|
| Đặt mục tiêu | SMART, OKR, 5W2H |
| Lập kế hoạch / phân rã nhiệm vụ | 5W2H, WBS, biểu đồ Gantt |
| Tìm nguyên nhân gốc rễ | 5Why, sơ đồ xương cá, quy tắc 80/20 |
| Ra quyết định / phân tích | SWOT, ma trận Eisenhower, sáu chiếc mũ tư duy, ma trận BCG, năm lực lượng Porter |
| Bám thực thi / cải tiến liên tục | PDCA, DMAIC, 8D |
| Giao tiếp và trình bày | Tháp nguyên lý, vòng tròn vàng |
| Rút kinh nghiệm | Phương pháp hoàn tất GRAI |
| Phân tích chất lượng nhà máy | QC 7 công cụ, sơ đồ kiểm soát, CPK, GRR, FMEA |
| Hiện trường & thiết bị | 5S, Poka-Yoke, TPM, OEE, SMED |
| Hiệu suất dây chuyền & logistics | Cân bằng dây chuyền, Kanban, VSM, EOQ |
| Quản lý hiện trường & thay đổi | Tam Hiện (Gemba), Quản lý thay đổi 4M, Quản lý bằng mắt |
| Kiểm tra & hệ thống | AQL, Kế hoạch kiểm soát, SDCA, FIFO |
| Nhu cầu & chiến lược | Kano, PEST, Ma trận Ansoff |
| Lãnh đạo đội nhóm | RACI, GROW, KPT, 5 chiến lược xung đột, Maslow |
| Dự án & rủi ro | Đường găng (CPM), Ma trận rủi ro |
| An toàn sản xuất | Quy tắc Heinrich |
| Hoạt động cải tiến | QCC, báo cáo A3 |

## Lộ trình chọn công cụ

```mermaid
flowchart TB
    Q{"Bạn đang cần làm gì?"}
    Q --> A["Đặt mục tiêu"] --> A1["SMART / OKR"]
    Q --> B["Lập kế hoạch"] --> B1["5W2H / WBS / Gantt"]
    Q --> C["Tìm nguyên nhân"] --> C1["5Why / sơ đồ xương cá"]
    Q --> D["Ra quyết định"] --> D1["SWOT / tứ tượng / sáu mũ tư duy"]
    Q --> E["Bám thực thi"] --> E1["PDCA / DMAIC / 8D"]
    Q --> F["Rút kinh nghiệm"] --> F1["GRAI / tháp nguyên lý"]
    Q --> G["Chất lượng & thiết bị nhà máy"] --> G1["QC 7 công cụ / CPK / GRR / 5S / TPM"]
    Q --> H["Lãnh đạo đội nhóm / Quản lý dự án"] --> H1["RACI / GROW / KPT / Ma trận rủi ro"]
    style Q fill:#dae8fc,stroke:#6c8ebf
```

---

## I. Nhóm mục tiêu và kế hoạch

### 1. Nguyên tắc SMART (đặt mục tiêu)

**Một câu**: Mục tiêu tốt phải cụ thể, có thể đo lường, khả thi, liên quan và có thời hạn.

```mermaid
flowchart LR
    G["Mục tiêu SMART"] --> S["S Cụ thể Specific<br/>Rõ ràng, không mơ hồ"]
    G --> M["M Có thể đo lường Measurable<br/>Có con số, có thể kiểm chứng"]
    G --> A["A Khả thi Achievable<br/>Với tới được khi nỗ lực"]
    G --> R["R Liên quan Relevant<br/>Căn chỉnh với mục tiêu tổng thể"]
    G --> T["T Có hạn Time-bound<br/>Có deadline rõ ràng"]
    style G fill:#dae8fc,stroke:#6c8ebf
    style S fill:#d5e8d4,stroke:#82b366
    style M fill:#ffe6cc,stroke:#d79b00
    style A fill:#fff2cc,stroke:#d6b656
    style R fill:#e1d5e7,stroke:#9673a6
    style T fill:#f8cecc,stroke:#b85450
```

**Ví dụ sai**: "Nâng cao sự hài lòng của khách hàng" (mơ hồ)
**Ví dụ đúng**: "Trong 3 tháng, giảm thời gian phản hồi lần đầu của tổ CSKH từ 4 giờ xuống dưới 1 giờ" (đáp ứng đủ SMART)

---

### 2. Phân tích 5W2H (nghĩ kỹ một việc)

**Một câu**: Dùng 7 câu hỏi để làm rõ toàn cảnh nhiệm vụ / phương án, tránh bỏ sót và làm việc mù quáng.

```mermaid
flowchart TB
    C["5W2H - Bảy câu hỏi phân tích"]
    C --> W1["What Làm gì?<br/>Nội dung và mục tiêu nhiệm vụ"]
    C --> W2["Why Tại sao?<br/>Lý do và mục đích"]
    C --> W3["Who Ai làm?<br/>Người chịu trách nhiệm và bên phối hợp"]
    C --> W4["When Khi nào?<br/>Thời gian và thời hạn"]
    C --> W5["Where Ở đâu?<br/>Địa điểm và phạm vi"]
    C --> H1["How Làm như thế nào?<br/>Phương pháp và lộ trình"]
    C --> H2["How much Bao nhiêu?<br/>Chi phí và lợi ích"]
    style C fill:#dae8fc,stroke:#6c8ebf
    style H2 fill:#ffe6cc,stroke:#d79b00
```

**Khi nào dùng**: giao nhiệm vụ, viết đề án, báo cáo, kiểm tra bỏ sót khi rút kinh nghiệm.

---

### 3. OKR (mục tiêu và kết quả then chốt)

**Một câu**: O là mục tiêu định tính, có tính thách thức và truyền cảm hứng; KR là kết quả định lượng để đo mức độ hoàn thành mục tiêu.

```mermaid
flowchart TB
    O["O Mục tiêu (định tính, có thách thức)<br/>Trở thành nhà cung cấp đáng tin cậy nhất của khách hàng trong quý này"]
    O --> KR1["KR1 Tỷ lệ giao hàng đúng hạn ≥ 98%"]
    O --> KR2["KR2 Tỷ lệ phản hồi khiếu nại trong 24 giờ đạt 100%"]
    O --> KR3["KR3 Điểm hài lòng của khách hàng ≥ 4.5"]
    style O fill:#dae8fc,stroke:#6c8ebf
    style KR1 fill:#d5e8d4,stroke:#82b366
    style KR2 fill:#d5e8d4,stroke:#82b366
    style KR3 fill:#d5e8d4,stroke:#82b366
```

**Điểm cần nhớ**: 1 O kèm 3-5 KR; hoàn thành 60-70% là tốt nhất (chứng tỏ mục tiêu có thách thức); không gắn trực tiếp với thưởng.

---

### 4. WBS - Cấu trúc phân rã công việc (chia nhỏ nhiệm vụ)

**Một câu**: Chia dự án lớn thành các nhiệm vụ nhỏ theo từng cấp "kết quả có thể giao nhận", đến mức "có thể thực hiện, phân công và ước tính" được.

```mermaid
flowchart TB
    P["Dự án: Tiệc cuối năm công ty"] --> A["1 Lập kế hoạch"]
    P --> B["2 Địa điểm"]
    P --> C["3 Chương trình"]
    P --> D["4 Hậu cần"]
    A --> A1["1.1 Xác định chủ đề"]
    A --> A2["1.2 Lập ngân sách"]
    B --> B1["2.1 So sánh khách sạn"]
    B --> B2["2.2 Ký hợp đồng"]
    C --> C1["3.1 Thu thập tiết mục"]
    C --> C2["3.2 Tổng duyệt"]
    D --> D1["4.1 Sắp xếp ăn uống"]
    D --> D2["4.2 Điều phối xe"]
    style P fill:#dae8fc,stroke:#6c8ebf
```

**Điểm cần nhớ**: Nguyên tắc 100% — phân rã phải bao quát toàn bộ công việc của dự án; nhiệm vụ tầng dưới cùng nên hoàn thành trong 1-2 ngày.

---

### 5. Biểu đồ Gantt (lập tiến độ)

**Một câu**: Trên trục thời gian ngang, nhìn thấy rõ "ai làm gì vào lúc nào, quan hệ phụ thuộc ra sao".

```mermaid
gantt
    title Kế hoạch dự án cải tiến website - ví dụ
    dateFormat YYYY-MM-DD
    section Lập kế hoạch
    Khảo sát nhu cầu     :a1, 2026-11-01, 7d
    Thiết kế phương án     :a2, after a1, 5d
    section Thực thi
    Phát triển         :b1, after a2, 10d
    Tích hợp và kiểm thử     :b2, after b1, 5d
    section Kết thúc
    Triển khai lên môi trường thật     :c1, after b2, 2d
    Rút kinh nghiệm     :c2, after c1, 3d
```

**Khi nào dùng**: lập lịch dự án, phối hợp liên phòng ban, báo cáo tiến độ với cấp trên.

---

## II. Nhóm phân tích vấn đề

### 6. Phân tích 5Why (truy nguyên nhân gốc rễ)

**Một câu**: Liên tục hỏi "tại sao" để xuyên qua biểu hiện, tìm ra nguyên nhân gốc rễ có thể hành động.

```mermaid
flowchart TB
    Q0["Vấn đề: Máy trên chuyền sản xuất dừng"]
    Q1["Why 1: Tại sao dừng?<br/>Cầu chì quá tải cháy"]
    Q2["Why 2: Tại sao quá tải?<br/>Bơm bôi trơn chạy quá tải"]
    Q3["Why 3: Tại sao bơm quá tải?<br/>Trục bơm mòn, quay không trơn"]
    Q4["Why 4: Tại sao trục mòn?<br/>Mạt sắt lọt vào hệ thống bôi trơn"]
    Q5["Why 5: Tại sao có mạt sắt?<br/>Chưa lắp bộ lọc ← Nguyên nhân gốc rễ"]
    A["Đối sách: Lắp bộ lọc, giải quyết triệt để"]
    Q0 --> Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> A
    style Q5 fill:#f8cecc,stroke:#b85450
    style A fill:#d5e8d4,stroke:#82b366
```

**Điểm cần nhớ**: Hỏi "tại sao" không phải để đổ lỗi; mỗi mắt xích nhân quả cần có bằng chứng, nếu không trả lời được thì dừng lại đi tìm dữ liệu.

---

### 7. Sơ đồ xương cá / sơ đồ Ishikawa (tìm nguyên nhân toàn diện)

**Một câu**: Từ các chiều Người - Máy - Nguyên liệu - Phương pháp - Môi trường, liệt kê mọi nguyên nhân có thể, tránh chỉ nhìn một hướng.

```mermaid
flowchart LR
    M1["Người Man<br/>Kỹ năng, thái độ, số lượng"] --> P(("Vấn đề chất lượng sản phẩm"))
    M2["Máy Machine<br/>Thiết bị, công cụ, bảo trì"] --> P
    M3["Nguyên liệu Material<br/>Vật tư, nhà cung cấp"] --> P
    M4["Phương pháp Method<br/>Quy trình, tiêu chuẩn, đào tạo"] --> P
    M5["Môi trường Environment<br/>Nhiệt độ, ánh sáng, khu vực sản xuất"] --> P
    style P fill:#f8cecc,stroke:#b85450
```

**Cách dùng**: Trước phát tán (brainstorm điền đầy các "xương"), sau đó thu hẹp và dùng 5Why đào sâu những "xương" đáng ngờ nhất. Tại hiện trường sản xuất thường dùng 4M1E / 6M (thêm Đo lường Measurement và Tự nhiên Mother Nature).

---

### 8. Quy tắc 80/20 / Pareto (nắm mâu thuẫn chính)

**Một câu**: 80% kết quả thường do 20% yếu tố then chốt quyết định, hãy tìm ra 20% đó trước.

```mermaid
flowchart LR
    A["20% số ít then chốt<br/>Khách hàng chính / vấn đề cốt lõi / công việc giá trị cao"] --> B["Đóng góp 80% doanh số / tổn thất"]
    C["80% số đông tầm thường"] --> D["Chỉ đóng góp 20% kết quả"]
    style A fill:#ffe6cc,stroke:#d79b00
    style B fill:#d5e8d4,stroke:#82b366
    style C fill:#f5f5f5,stroke:#999999
    style D fill:#f5f5f5,stroke:#999999
```

**Khi nào dùng**: sắp xếp thứ tự ưu tiên, tìm điểm tập trung của vấn đề chất lượng (biểu đồ Pareto), quản lý thời gian (ăn con ếch trước).

---

## III. Nhóm ra quyết định và phân tích

### 9. Phân tích SWOT (định hướng chiến lược)

**Một câu**: Đưa điểm mạnh / yếu nội bộ và cơ hội / đe dọa bên ngoài lên một mặt bằng, từ đó kết hợp thành chiến lược hành động.

```mermaid
quadrantChart
    title Phân tích SWOT - trục ngang: nội bộ → bên ngoài; trục dọc: có lợi → bất lợi
    x-axis "Nội bộ" --> "Bên ngoài"
    y-axis "Có lợi" --> "Bất lợi"
    quadrant-2 "Điểm mạnh S"
    quadrant-1 "Đe dọa T"
    quadrant-3 "Cơ hội O"
    quadrant-4 "Điểm yếu W"
```

**Ví dụ**: Điểm mạnh = công nghệ mạnh, thương hiệu tốt; Điểm yếu = kênh phân phối yếu, thiếu nhân tài; Cơ hội = chính sách hỗ trợ, thị trường tăng trưởng; Đe dọa = cạnh tranh gay gắt, sản phẩm thay thế xuất hiện.

**Chiến lược tổ hợp bốn tượng**:

| Tổ hợp | Chiến lược | Ý nghĩa |
|---|---|---|
| S + O | SO - Tăng trưởng | Dùng điểm mạnh nắm cơ hội, tấn công toàn lực |
| W + O | WO - Chuyển đổi | Bù đắp điểm yếu để tận dụng cơ hội |
| S + T | ST - Phòng thủ | Dùng điểm mạnh chống lại đe dọa |
| W + T | WT - Thu hẹp | Giảm đầu tư, ưu tiên tồn tại trước |

---

### 10. Ma trận Eisenhower (quản lý thời gian)

**Một câu**: Phân loại theo "quan trọng / khẩn cấp", dành năng lượng cho việc "quan trọng nhưng không khẩn cấp".

```mermaid
quadrantChart
    title Ma trận Eisenhower - trục ngang: khẩn cấp → không khẩn cấp; trục dọc: không quan trọng → quan trọng
    x-axis "Khẩn cấp" --> "Không khẩn cấp"
    y-axis "Không quan trọng" --> "Quan trọng"
    quadrant-2 "① Làm ngay"
    quadrant-1 "② Lập kế hoạch làm （tập trung đầu tư）"
    quadrant-3 "③ Ủy quyền / xử lý nhanh"
    quadrant-4 "④ Hạn chế / không làm"
```

- **① Quan trọng + Khẩn cấp** (khủng hoảng, nhiệm vụ sắp đến hạn) → Làm ngay
- **② Quan trọng + Không khẩn cấp** (hoạch định, học tập, phòng ngừa, rèn luyện) → Làm có kế hoạch, **giá trị cao nhất**
- **③ Không quan trọng + Khẩn cấp** (bị gián đoạn đột xuất, một số cuộc họp) → Ủy quyền hoặc xử lý nhanh
- **④ Không quan trọng + Không khẩn cấp** (lướt mạng vô mục đích, tán gẫu) → Giảm thiểu hoặc không làm

**Insight cốt lõi**: Người làm việc hiệu quả dành phần lớn thời gian cho ô Q2; ô Q1 liên tục bốc cháy chính vì Q2 làm chưa đủ.

---

### 11. Sáu chiếc mũ tư duy (thảo luận nhóm)

**Một câu**: Mỗi lần chỉ đội một mũ, chỉ dùng một kiểu tư duy để thảo luận, tránh cãi vã và rối loạn tư duy.

```mermaid
flowchart LR
    M["Chủ đề"] --- W1["Mũ trắng<br/>Sự kiện và dữ liệu khách quan"]
    M --- W2["Mũ đỏ<br/>Trực giác và cảm xúc"]
    M --- W3["Mũ đen<br/>Rủi ro và phê phán"]
    M --- W4["Mũ vàng<br/>Giá trị và lợi ích"]
    M --- W5["Mũ xanh lá<br/>Sáng tạo và phương án mới"]
    M --- W6["Mũ xanh dương<br/>Quy trình và tổng kết"]
    style W1 fill:#f5f5f5,stroke:#999999
    style W2 fill:#f8cecc,stroke:#b85450
    style W3 fill:#333333,color:#ffffff
    style W4 fill:#ffe6cc,stroke:#d79b00
    style W5 fill:#d5e8d4,stroke:#82b366
    style W6 fill:#dae8fc,stroke:#6c8ebf
```

**Trình tự điển hình**: Xanh dương (định quy trình) → Trắng (đưa ra sự thật) → Xanh lá (đề xuất phương án) → Vàng (nhìn giá trị) → Đen (tìm rủi ro) → Đỏ (bày tỏ thái độ) → Xanh dương (kết luận).

---

### 12. Ma trận BCG (quyết định danh mục kinh doanh)

**Một câu**: Chia doanh nghiệp thành bốn nhóm theo "tốc độ tăng trưởng thị trường × thị phần tương đối", từ đó quyết định đầu tư hay thu hoạch.

```mermaid
quadrantChart
    title Ma trận BCG - trục ngang: thị phần tương đối thấp → cao; trục dọc: tốc độ tăng trưởng thị trường thấp → cao
    x-axis "Thị phần thấp" --> "Thị phần cao"
    y-axis "Tăng trưởng thấp" --> "Tăng trưởng cao"
    quadrant-2 "Dấu hỏi：chọn lọc đầu tư"
    quadrant-1 "Ngôi sao：tăng đầu tư"
    quadrant-3 "Chó săn：thu hẹp hoặc rút lui"
    quadrant-4 "Bò sữa：thu tiền mặt, nuôi ngôi sao"
```

---

### 13. Mô hình năm lực lượng Porter (phân tích cạnh tranh ngành)

**Một câu**: Sức hấp dẫn của ngành do năm lực lượng quyết định, phân tích rõ rồi mới quyết định có nên vào, vào bằng cách nào.

```mermaid
flowchart TB
    T1["Cạnh tranh giữa các đối thủ hiện tại<br/>Mức độ tập trung, chiến tranh giá"] --- C(("Tiềm năng lợi nhuận<br/>cổ ngành"))
    T2["Sức mạnh thương lượng của nhà cung cấp"] --- C
    T3["Sức mạnh thương lượng của người mua"] --- C
    T4["Đe dọa từ người mới gia nhập<br/>Rào cản cao hay thấp"] --- C
    T5["Đe dọa từ sản phẩm thay thế"] --- C
    style C fill:#dae8fc,stroke:#6c8ebf
```

**Năm lực lượng càng mạnh, lợi nhuận trung bình của ngành càng thấp.**

---

### 14. Nguyên tắc MECE (phân rã có cấu trúc)

**Một câu**: Phân loại phải đạt "loại trừ lẫn nhau, bao quát toàn bộ" — không trùng, không sót.

```mermaid
flowchart TB
    T["Vấn đề: Làm sao nâng cao sự hài lòng của người dùng?"] --> A["Trải nghiệm sản phẩm"]
    T --> B["Yếu tố giá cả"]
    T --> C["Chất lượng dịch vụ"]
    A --- B
    B --- C
    style T fill:#dae8fc,stroke:#6c8ebf
    style A fill:#d5e8d4,stroke:#82b366
    style B fill:#ffe6cc,stroke:#d79b00
    style C fill:#e1d5e7,stroke:#9673a6
```

**Cách kiểm tra**: Lấy hai hạng mục bất kỳ ghép lại, nếu có thể gộp thì chưa loại trừ lẫn nhau; nếu có thể đưa ra phản ví dụ thì chưa bao quát toàn bộ. Đây là kỹ năng nền của tháp nguyên lý và tư vấn theo phong cách McKinsey.

---

## IV. Nhóm giao tiếp và trình bày

### 15. Tháp nguyên lý / SCQA (báo cáo và viết lách)

**Một câu**: Kết luận đi trước, trên dưới thống nhất, phân nhóm có hệ thống, logic tiến triển.

```mermaid
flowchart TB
    S1["S Bối cảnh Situation<br/>Trước hết trình bày bối cảnh cả hai bên đều công nhận"] --> C1["C Xung đột Complication<br/>Có thay đổi / vấn đề gì xảy ra"]
    C1 --> Q1["Q Câu hỏi Question<br/>Dẫn dắt tự nhiên đến câu hỏi then chốt"]
    Q1 --> A1["A Trả lời Answer<br/>Đưa ra kết luận và phương án (nói trọng tâm trước)"]
    style A1 fill:#d5e8d4,stroke:#82b366
```

**So sánh**: "Sếp, ngân sách, nhân sự, tiến độ là như vậy… nên em muốn xin thêm người" (vòng vo lâu)
**SCQA**: "Sếp, dự án có nguy cơ chậm tiến độ (C). Em đề xuất bổ sung 2 lập trình viên (A). Lý do là… (chi tiết S+Q)"

---

### 16. Vòng tròn vàng - Golden Circle (truyền cảm hứng)

**Một câu**: Tổ chức xuất sắc bắt đầu truyền thông từ "tại sao", tổ chức tầm thường chỉ nói "làm gì".

```mermaid
flowchart TB
    WHY["WHY Tại sao làm<br/>Sứ mệnh, niềm tin (thuyết phục người)"] --> HOW["HOW Làm như thế nào<br/>Phương pháp, điểm khác biệt"] --> WHAT["WHAT Làm gì<br/>Sản phẩm, kết quả (ai cũng nói được)"]
    style WHY fill:#f8cecc,stroke:#b85450
    style HOW fill:#ffe6cc,stroke:#d79b00
    style WHAT fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Apple không nói "Chúng tôi làm máy tính (What)", mà nói "Chúng tôi tin vào việc thách thức hiện trạng (Why), vì vậy chúng tôi thiết kế theo cách khác biệt (How), tạo ra những chiếc máy tính dễ dùng (What)".

---

## V. Nhóm thực thi và cải tiến

### 17. Vòng lặp PDCA (cải tiến liên tục)

**Một câu**: Kế hoạch — Thực hiện — Kiểm tra — Hành động, lặp đi lặp lại không ngừng, mỗi vòng lên một bậc.

```mermaid
flowchart LR
    P["① Plan Lập kế hoạch<br/>Tìm vấn đề, đặt mục tiêu, định phương án"] --> D["② Do Thực hiện<br/>Triển khai nhỏ, ghi dữ liệu"]
    D --> C["③ Check Kiểm tra<br/>So sánh với mục tiêu, tìm độ lệch"]
    C --> A["④ Act Xử lý<br/>Tiêu chuẩn hóa; vấn đề còn lại chuyển sang vòng sau"]
    A -->|"Vòng mới, thăng tiến từng bậc"| P
    style P fill:#dae8fc,stroke:#6c8ebf
    style D fill:#d5e8d4,stroke:#82b366
    style C fill:#ffe6cc,stroke:#d79b00
    style A fill:#f8cecc,stroke:#b85450
```

**Điểm cần nhớ**: Check là khâu nhiều người bỏ qua; trong Act, những cách làm đã được chứng minh hiệu quả cần được cố định thành tiêu chuẩn (đây là nền tảng của cải tiến "vòng lớn lồng vòng nhỏ").

---

### 18. DMAIC (quy trình cải tiến Six Sigma)

**Một câu**: Dùng quy trình 5 bước dựa trên dữ liệu để giải quyết vấn đề chất lượng phức tạp, nặng đo lường và thống kê hơn PDCA.

```mermaid
flowchart LR
    D["Define Định nghĩa<br/>Làm rõ vấn đề và nhu cầu khách hàng"] --> M["Measure Đo lường<br/>Thu thập dữ liệu, định lượng hiện trạng"]
    M --> A["Analyze Phân tích<br/>Dùng phương pháp thống kê tìm nguyên nhân chính"]
    A --> I["Improve Cải tiến<br/>Thiết kế và kiểm chứng giải pháp"]
    I --> C["Control Kiểm soát<br/>Cố định tiêu chuẩn, giám sát chống tái phát"]
    C -.->|"Giám sát liên tục"| D
    style D fill:#dae8fc,stroke:#6c8ebf
    style M fill:#d5e8d4,stroke:#82b366
    style A fill:#ffe6cc,stroke:#d79b00
    style I fill:#e1d5e7,stroke:#9673a6
    style C fill:#f8cecc,stroke:#b85450
```

**Khi nào dùng**: cải tiến chất lượng sản xuất, tỷ lệ lỗi quy trình cao, vấn đề phức tạp có đủ dữ liệu.

---

### 19. Báo cáo 8D (xử lý khiếu nại / sự cố chất lượng)

**Một câu**: Quy trình giải quyết vấn đề theo nhóm chuẩn của ngành ô tô, D3 cầm máu trước, D4-D5 mới trị gốc rễ.

```mermaid
flowchart TB
    D0["D0 Chuẩn bị: đánh giá có cần 8D không"] --> D1["D1 Thành lập đội xử lý"]
    D1 --> D2["D2 Mô tả vấn đề (5W2H)"]
    D2 --> D3["D3 Biện pháp tạm thời ngăn chặn (cầm máu)"]
    D3 --> D4["D4 Phân tích nguyên nhân gốc rễ (5Why / sơ đồ xương cá)"]
    D4 --> D5["D5 Biện pháp khắc phục lâu dài"]
    D5 --> D6["D6 Kiểm chứng hiệu quả biện pháp"]
    D6 --> D7["D7 Phòng ngừa tái phát (tiêu chuẩn hóa)"]
    D7 --> D8["D8 Ghi nhận đội, đóng vấn đề"]
    style D3 fill:#ffe6cc,stroke:#d79b00
    style D5 fill:#d5e8d4,stroke:#82b366
```

**Lưu ý**: Chưa D3 cầm máu đã bàn trị gốc rễ giống như vừa mổ vừa để máu chảy.

---

### 20. Phương pháp hoàn tất GRAI (biến kinh nghiệm thành năng lực)

**Một câu**: Mục tiêu — Kết quả — Phân tích — Kết luận, bốn bước biến "chuyện đã xảy ra" thành "kinh nghiệm dùng được lần sau".

```mermaid
flowchart LR
    G["G Goal Hồi tưởng mục tiêu<br/>Ban đầu muốn đạt gì?"] --> R["R Result Đánh giá kết quả<br/>Thực tế xảy ra gì? Khoảng cách ở đâu?"]
    R --> A["A Analysis Phân tích nguyên nhân<br/>Nguyên nhân gốc rễ của đúng/sai"]
    A --> I["I Insight Tổng kết kinh nghiệm<br/>Quy luật tái sử dụng, việc nên dừng / tiếp tục / bắt đầu"]
    I --> G2["Chuyển sang mục tiêu vòng tiếp theo (vòng kín PDCA)"]
    style G fill:#dae8fc,stroke:#6c8ebf
    style R fill:#d5e8d4,stroke:#82b366
    style A fill:#ffe6cc,stroke:#d79b00
    style I fill:#f8cecc,stroke:#b85450
```

**Điểm then chốt**: Hoàn tất không phải họp đổ lỗi, chỉ bàn việc không bàn người; Insight phải cụ thể thành "lần sau làm như thế nào".

---

## VI. Nhóm quản lý chất lượng: QC 7 công cụ

### 21. Tổng quan QC 7 công cụ

**Một câu**: "Bộ công cụ cơ bản" để cải tiến chất lượng tại hiện trường — 5 công cụ dùng để mô tả vấn đề, 2 công cụ dùng để phân tích nguyên nhân.

```mermaid
flowchart TB
    ROOT["QC 7 công cụ"]
    ROOT --> D1["Mô tả vấn đề (dữ liệu nói)"]
    ROOT --> D2["Phân tích vấn đề (tìm nguyên nhân)"]
    D1 --> T1["Phiếu kiểm tra<br/>Thu thập dữ liệu"]
    D1 --> T2["Phân tầng<br/>Phân loại so sánh"]
    D1 --> T3["Pareto<br/>Nắm số ít then chốt"]
    D1 --> T4["Histogram<br/>Nhìn hình dạng phân bố"]
    D1 --> T5["Sơ đồ phân tán<br/>Xem quan hệ hai biến"]
    D1 --> T6["Sơ đồ kiểm soát<br/>Giám sát dao động quy trình"]
    D2 --> T7["Sơ đồ nhân quả (xương cá)<br/>Tìm nguyên nhân có hệ thống"]
    style ROOT fill:#dae8fc,stroke:#6c8ebf
```

| Công cụ | Trả lời câu hỏi | Cách dùng điển hình |
|---|---|---|
| Phiếu kiểm tra | Hiện trạng thực ra thế nào? | Ghi chép số lượng lỗi theo từng hạng mục |
| Phân tầng | Loại vấn đề nào tập trung nhất? | Phân theo ca, máy, khuôn, vật liệu, người vận hành |
| Pareto | Giải quyết trước cái nào? | Top 2-3 hạng mục thường chiếm 80% lỗi |
| Histogram | Quy trình ổn định không? | Xem hình dạng phân bố, so sánh với giới hạn quy cách |
| Sơ đồ phân tán | A và B có quan hệ không? | Nhiệt độ vs tỷ lệ lỗi, tốc độ vs độ mòn |
| Sơ đồ kiểm soát | Quy trình hiện tại bình thường không? | Giám sát thời gian thực, cảnh báo khi vượt giới hạn |
| Sơ đồ xương cá | Tại sao xảy ra? | Kết hợp 5Why tìm nguyên nhân gốc rễ (xem mục 7) |

---

### 22. Phiếu kiểm tra (Check Sheet)

**Một câu**: Biến "dựa vào cảm tính" thành "dựa vào dữ liệu", ghi chép từng hạng mục theo mẫu thiết kế sẵn.

**Ví dụ: Phiếu kiểm tra lỗi ép nhựa (ghi mỗi 2 giờ)**

| Thời gian | Số lô | Số kiểm | Thiếu liệu | Burr | Co rút | Đốm đen | Tổng |
|---|---|---|---|---|---|---|---|
| 08:00 | A-101 | 50 | 1 | 0 | 2 | 0 | 3 |
| 10:00 | A-101 | 50 | 0 | 3 | 1 | 1 | 5 |
| 12:00 | A-102 | 50 | 2 | 1 | 0 | 0 | 3 |

**Điểm cần nhớ**: Tên hạng mục phải cụ thể ("thiếu liệu" thay vì "lỗi ngoại quan"); cuối ngày tổng hợp có thể chuyển thẳng thành Pareto.

---

### 23. Phân tầng (Stratification)

**Một câu**: Tách dữ liệu hỗn hợp theo chiều so sánh, sự khác biệt thường lộ rõ ngay.

**Ví dụ**: Tỷ lệ lỗi toàn nhà máy 3.2% trông có vẻ đều, nhưng khi phân tầng theo máy:

| Máy | 1# | 2# | 3# | 4# |
|---|---|---|---|---|
| Tỷ lệ lỗi | 1.1% | 1.3% | **8.9%** | 1.5% |

→ Vấn đề thu hẹp vào máy 3# (điều tra tiếp: khuôn máy này mòn + chưa căn chỉnh sau đổi khuôn).

**Chiều phân tầng thường dùng**: ca làm việc, máy, khuôn, lô vật liệu, nhà cung cấp, người vận hành, thiết bị đo, nhiệt độ / độ ẩm môi trường.

---

### 24. Pareto

**Một câu**: Sắp xếp số lượng lỗi từ lớn đến nhỏ, tập trung vào 20% hạng mục để giải quyết 80% vấn đề.

```mermaid
xychart-beta
    title "Pareto lỗi ép nhựa - một tuần, n=92"
    x-axis ["Thiếu liệu", "Burr", "Co rút", "Đốm đen", "Khác"]
    bar [45, 22, 12, 9, 4]
```

**Tỷ lệ tích lũy**: Thiếu liệu 49% → cộng Burr 73% → cộng Co rút 86%. Cải tiện hai hạng mục "Thiếu liệu + Burr" là giải quyết gần ba phần tư số lỗi.

**Điểm cần nhớ**: Pareto sau khi phân tầng (ví dụ vẽ riêng từng máy) còn mạnh hơn nhiều.

---

### 25. Histogram

**Một câu**: Chia giá trị đo thành các nhóm và vẽ thành cột, nhìn một cái là thấy trung tâm và độ phân tán của quy trình.

```mermaid
xychart-beta
    title "Histogram đường kính ngoài trục - n=100, quy cách φ10±0.05"
    x-axis ["9.96", "9.98", "10.00", "10.02", "10.04", "10.06"]
    bar [4, 18, 35, 28, 11, 4]
```

**Đọc biểu đồ**: Trung tâm khoảng 10.005, gần như nằm giữa quy cách; phân bố gần dạng chuông → năng lực quy trình tốt. Nếu cột xuất hiện hai đỉnh, đảo hoặc lệch một bên, lần lượt gợi ý: trộn lẫn hai máy / có giá trị bất thường / cần căn chỉnh máy.

---

### 26. Sơ đồ phân tán (Scatter Diagram)

**Một câu**: Xem hai biến số có quan hệ tương quan hay không, và là dạng quan hệ gì.

| Dạng | Ý nghĩa | Hướng xử lý |
|---|---|---|
| Tương quan dương mạnh (↗) | A tăng thì B tăng | Kiểm soát A là kiểm soát B |
| Tương quan âm mạnh (↘) | A tăng thì B giảm | Tương tự như trên |
| Không tương quan (phân tán) | Hai bên không liên quan | Tìm nguyên nhân khác |
| Tương quan phi tuyến (∩) | Quan hệ không tuyến tính | Tìm điểm uốn / giá trị tối ưu |

**Ví dụ**: Ghi 12 cặp "nhiệt độ phễu nhựa vs số lỗi thiếu liệu", tính hệ số tương quan r=0.85 (tương quan dương mạnh) → nhiệt độ là một trong những nguyên nhân chính, sau đó dùng thử nghiệm DOE khóa giá trị tối ưu 235℃.

---

### 27. Sơ đồ kiểm soát (Control Chart / SPC)

**Một câu**: Vẽ "vùng dao động bình thường" cho quy trình, khi vượt giới hạn hoặc sắp xếp bất thường thì báo động — phát hiện sớm hơn kiểm tra hậu kiểm.

```mermaid
xychart-beta
    title "Sơ đồ kiểm soát X - mục tiêu 10.0, giới hạn kiểm soát ±0.5"
    x-axis [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    line [10.1, 9.9, 10.2, 10.0, 9.8, 10.3, 10.1, 9.9, 10.0, 10.2, 10.1, 11.2]
    line [10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5, 10.5]
    line [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
    line [9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5, 9.5]
```

**Đọc biểu đồ**: Bốn đường lần lượt là — giá trị đo (đường gấp khúc), giới hạn kiểm soát trên UCL, đường trung tâm CL, giới hạn kiểm soát dưới LCL. Điểm thứ 12 vượt UCL → bất thường! Dừng chuyền ngay để điều tra (ví dụ: dao cắt mòn).

**Quy tắc nhận biết bất thường thường gặp**: 1 điểm ra ngoài giới hạn / 7 điểm liên tiếp cùng bên / 7 điểm liên tiếp tăng hoặc giảm / 3 điểm trong đó 2 điểm gần giới hạn kiểm soát.

---

## VII. Nhóm năng lực quy trình: CPK

### 28. CPK / PPK - Chỉ số năng lực quy trình

**Một câu**: Không chỉ "làm ra đều đạt" (Cp xem độ phân tán), mà còn phải "quy trình luôn nằm giữa" (Cpk xem độ lệch tâm).

```mermaid
flowchart LR
    A["Quy cách: đường kính trục φ10 ± 0.05<br/>USL=10.05, LSL=9.95"] --> B["Thu thập dữ liệu n≥100<br/>Tính trung bình μ và độ lệch chuẩn σ"]
    B --> C["Cp = (USL - LSL) / 6σ<br/>= 0.10 / 0.048 ≈ 2.08"]
    B --> D["Cpk = min(USL-μ, μ-LSL) / 3σ<br/>μ=10.01 → min(0.04, 0.06)/0.024 ≈ 1.67"]
    C --> E{"Năng lực đủ không?"}
    D --> E
    E -->|"Cpk ≥ 1.67"| F["Xuất sắc<br/>Có thể miễn kiểm / giảm tần suất kiểm"]
    E -->|"1.33 ~ 1.67"| G["Đạt<br/>Sản xuất hàng loạt bình thường + SPC"]
    E -->|"< 1.33"| H["Chưa đủ<br/>Cải tiến công nghệ hoặc kiểm tra 100%"]
    style F fill:#d5e8d4,stroke:#82b366
    style G fill:#ffe6cc,stroke:#d79b00
    style H fill:#f8cecc,stroke:#b85450
```

**Khác biệt then chốt**: Cp chỉ so "độ phân tán vs dải công sai", không quan tâm lệch tâm; Cpk còn phạt thêm độ lệch tâm. Ví dụ: σ giống nhau nhưng μ lệch về 10.04, Cp vẫn 2.08, Cpk tụt xuống 0.14 (siêu sai nhiều) — **sản xuất hàng loạt luôn đánh giá bằng Cpk**.

**Tiêu chuẩn tham khảo**: Cpk≥1.33 cho ngành thông thường; Cpk≥1.67 cho ô tô / chi tiết an toàn. PPK tính toán tương tự, dùng cho giai đoạn thử sản xuất (dữ liệu dài hạn chứa mọi biến động).

---

## VIII. Nhóm phân tích hệ thống đo lường: GRR

### 29. GRR (Gauge Repeatability & Reproducibility)

**Một câu**: Trước hết phải chứng minh bằng dữ liệu rằng "dụng cụ đo + người + phương pháp" đáng tin, nếu không CPK, SPC phía sau đều là xây nhà trên cát.

```mermaid
flowchart LR
    A["Chọn 10 chi tiết<br/>bao phủ toàn dải công sai"] --> B["3 kiểm tra viên<br/>mỗi người đo mỗi chi tiết 3 lần"]
    B --> C["Tính %GRR<br/>= biến thiên của hệ thống đo / biến thiên tổng"]
    C --> D{"Phán định"}
    D -->|"%GRR ＜ 10%"| E["Chấp nhận được<br/>Hệ thống đo đáng tin"]
    D -->|"10% ~ 30%"| F["Chấp nhận có điều kiện<br/>tùy mức độ quan trọng của đặc tính"]
    D -->|"＞ 30%"| G["Không chấp nhận<br/>Đổi dụng cụ / đào tạo / đổi phương pháp"]
    style E fill:#d5e8d4,stroke:#82b366
    style F fill:#ffe6cc,stroke:#d79b00
    style G fill:#f8cecc,stroke:#b85450
```

**Ví dụ**: Dùng thước kẹp điện tử đo đường kính trục φ10±0.05, thử nghiệm 10×3×3 cho %GRR=8.2% → chấp nhận được, dữ liệu của dụng cụ này có thể dùng để tính CPK. Nếu %GRR=35%, dù CPK tính ra 1.5 cũng không đáng tin — nhiễu đo đã che mờ biến thiên thực sự.

**Phân rã**: Lặp lại (Repeatability — biến động khi cùng một kiểm tra viên đo cùng một chi tiết, phản ánh bản thân dụng cụ) + Tái hiện (Reproducibility — chênh lệch giữa các kiểm tra viên, phản ánh yếu tố con người).

---

## IX. Nhóm phòng ngừa rủi ro và công cụ ngành ô tô

### 30. FMEA - Phân tích chế độ hỏng và hậu quả

**Một câu**: Ngay từ giai đoạn thiết kế liệt kê trước "chỗ nào có thể hỏng, hỏng nghiêm trọng mức nào, có chặn được không", sau đó sắp xếp theo rủi ro để ưu tiên phòng ngừa.

```mermaid
flowchart LR
    A["Nhận diện chế độ hỏng tiềm ẩn<br/>VD: Hàn chân không"] --> B["Chấm điểm (mỗi tiêu chí 1~10)<br/>S Mức độ nghiêm trọng · O Tần suất xảy ra · D Khả năng phát hiện"]
    B --> C["RPN = S × O × D<br/>VD: 8×4×3 = 96"]
    C --> D{"RPN ≥ 100 hoặc S ≥ 9?"}
    D -->|"Có"| E["Phải cải tiến<br/>Thêm Poka-Yoke / đổi thiết kế / tăng kiểm tra"]
    D -->|"Không"| F["Chấp nhận và giám sát"]
    E --> G["Chấm điểm lại sau cải tiến<br/>RPN phải giảm rõ rệt"]
    style C fill:#ffe6cc,stroke:#d79b00
```

**Ví dụ (trích FMEA hàn sóng bảng điều khiển)**:

| Chế độ hỏng | S | O | D | RPN | Biện pháp |
|---|---|---|---|---|---|
| Hàn chân không | 8 | 4 | 3 | 96 | Tăng kiểm tra AOI tự động |
| Lắp ngược cực tính | 9 | 2 | 5 | 90 | Đổi footprint PCB chống lắp ngược (xem Poka-Yoke) |
| Thiếu vặn ốc | 6 | 3 | 2 | 36 | Máy bắn vít đếm số + cảnh báo |

**Điểm cần nhớ**: S≥9 (rủi ro an toàn) bất kể RPN là bao nhiêu cũng phải sửa; phiên bản AIAG-VDA mới dùng AP (Action Priority) thay thế RPN, tư tưởng vẫn tương tự.

---

### 31. Năm công cụ IATF (ngành ô tô)

**Một câu**: APQP quản lý nhịp độ quy trình, FMEA quản lý rủi ro, SPC quản lý quy trình, MSA quản lý đo lường, PPAP quản lý phê duyệt sản xuất hàng loạt.

```mermaid
flowchart LR
    A["APQP Lập kế hoạch chất lượng sản phẩm ban đầu<br/>5 giai đoạn: Kế hoạch → Thiết kế → Mẫu → Thử sản xuất → Hàng loạt"] --> B["FMEA<br/>Phân tích rủi ro thiết kế / quy trình"]
    A --> C["SPC<br/>Giám sát đặc tính then chốt của quy trình"]
    A --> D["MSA<br/>Thẩm định hệ thống đo (bao gồm GRR)"]
    B --> E["PPAP Phê duyệt sản phẩm sản xuất<br/>Khách hàng đồng ý mới được sản xuất hàng loạt"]
    C --> E
    D --> E
    style A fill:#dae8fc,stroke:#6c8ebf
    style E fill:#d5e8d4,stroke:#82b366
```

**Tình huống thực tế**: Khi cung cấp cho khách hàng ô tô, bộ hồ sơ PPAP thường gồm: FMEA, kế hoạch kiểm soát, MSA (báo cáo GRR), năng lực quy trình ban đầu (Cpk), báo cáo mẫu.

---

## X. Nhóm hiện trường & thiết bị nhà máy

### 32. 5S - Quản lý hiện trường

**Một câu**: Sàng lọc, Sắp xếp, Sạch sẽ, Săn sóc, Sẵn sàng — mọi thứ trong quản lý hiện trường đều bắt đầu từ 5S.

```mermaid
flowchart LR
    S1["1S Sàng lọc<br/>Cần và không cần<br/>Loại bỏ dứt khoát"] --> S2["2S Sắp xếp<br/>Đúng vị trí, đúng dung lượng, đúng số lượng<br/>Tìm trong 30 giây"]
    S2 --> S3["3S Sạch sẽ<br/>Quét bụi, dầu mỡ<br/>Vừa sạch vừa kiểm tra"]
    S3 --> S4["4S Săn sóc<br/>Tiêu chuẩn hóa 3S đầu<br/>Duy trì thành quả"]
    S4 --> S5["5S Sẵn sàng<br/>Thành thói quen"]
    style S5 fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Thời gian tìm dụng cụ đổi khuôn giảm từ 20 phút xuống 2 phút — dụng cụ treo theo bảng mẫu (shadow board), thiếu là nhìn thấy ngay (kết hợp với Poka-Yoke).

---

### 33. Poka-Yoke (Phòng ngừa sai sót)

**Một câu**: Khiến lỗi "muốn phạm cũng không phạm được", thay vì trông chờ vào sự cẩn thận của con người.

| Loại Poka-Yoke | Nguyên lý | Ví dụ |
|---|---|---|
| Hình dạng | Bất đối xứng, lắp ngược không vừa | Cổng USB, chốt định vị bất đối xứng |
| Thứ tự | Chưa hoàn thành bước trước thì bước sau không làm được | Chưa lắp vỏ thì tuốc nơ vít không chạm được ốc |
| Đếm | Số lượng không đủ không cho qua | Máy bắn vít đủ 4 con mới báo đèn xanh |
| Cảnh báo | Bất thường báo động ngay lập tức | Thiếu linh kiện kéo Andon |
| Thông tin | Màu sắc / nhãn mác phân biệt tránh nhầm lẫn | Thùng đỏ / xanh tương ứng lô khác nhau |

**Ví dụ**: Nhân viên thường xuyên lắp thiếu gioăng cao su gây khiếu nại → đổi sang cấp liệu rung + đếm quang, thiếu gioăng máy tự dừng (Poka-Yoke dạng đếm + cảnh báo).

---

### 34. OEE - Hiệu suất thiết bị tổng hợp

**Một câu**: Tỷ lệ thời gian thiết bị thực sự tạo ra sản phẩm có giá trị, bằng tích của ba tổn thất lớn.

```mermaid
flowchart LR
    A["Thời gian tải 480 phút"] --> B["Trừ: Hỏng hóc + đổi khuôn 60 phút<br/>Hiệu suất thời gian 87.5%"]
    B --> C["Nhân: Tổn thất tốc độ<br/>Hiệu suất hiệu suất 95%"]
    C --> D["Nhân: Lỗi + tái chế<br/>Tỷ lệ hàng đạt 98%"]
    D --> E["OEE = 87.5% × 95% × 98%<br/>≈ 81.5%"]
    E --> F{"Mức thế giới 85%"}
    style E fill:#ffe6cc,stroke:#d79b00
```

**Sáu tổn thất nhanh**: Hỏng máy, đổi khuôn / căn chỉnh (thuộc "tổn thất thời gian"); Chạy không tải, giảm tốc (thuộc "tổn thất hiệu suất"); Phế phẩm khởi động, lỗi quy trình (thuộc "tổn thất chất lượng").

**Ví dụ**: Thiết bị có OEE chỉ 45%, ưu tiên dùng Pareto tìm tổn thất lớn nhất — nếu đổi khuôn chiếm 30%, làm SMED trước; nếu hỏng hóc chiếm 40%, làm TPM trước.

---

### 35. TPM - Bảo trì sản xuất toàn diện

**Một câu**: Người vận hành làm kiểm tra bảo dưỡng hàng ngày, kỹ thuật viên bảo trì làm chuyên môn, tiêu diệt hỏng hóc ngay từ khi còn là mầm mống.

```mermaid
flowchart TB
    ROOT["8 trụ cột TPM"]
    ROOT --> P1["Tự chủ bảo dưỡng<br/>Người vận hành: vệ sinh là kiểm tra"]
    ROOT --> P2["Bảo dưỡng có kế hoạch<br/>Kỹ thuật: bảo dưỡng định kỳ"]
    ROOT --> P3["Cải tiến riêng lẻ<br/>Tiêu diệt sáu tổn thất"]
    ROOT --> P4["Đào tạo<br/>Đào tạo công nhân đa kỹ năng"]
    ROOT --> P5["Quản lý giai đoạn đầu<br/>Thiết kế thiết bị mới ít cần bảo trì"]
    ROOT --> P6["Bảo đảm chất lượng<br/>Thiết bị không sản xuất hàng lỗi"]
    ROOT --> P7["Hiệu quả hóa bộ phận gián tiếp"]
    ROOT --> P8["An toàn · Môi trường<br/>Zero tai nạn"]
    style ROOT fill:#dae8fc,stroke:#6c8ebf
```

**Điểm khởi đầu**: Bắt đầu từ "bước 1 tự chủ bảo dưỡng — vệ sinh ban đầu": trong lúc lau chùi phát hiện ray máy 3# chảy dầu → báo sửa triệt để → thời gian dừng máy tháng đó giảm 40%.

---

### 36. SMED - Đổi khuôn nhanh

**Một câu**: Biến những việc đổi khuôn "phải dừng máy" thành "không cần dừng máy cũng làm được", giảm một nửa thời gian đổi khuôn là chuyện thường.

```mermaid
flowchart LR
    A["Hiện trạng: đổi khuôn 120 phút"] --> B["Bước 1: Tách nội / ngoại<br/>Nội bộ 70 / Ngoại bộ 50"]
    B --> C["Bước 2: Chuyển nội ra ngoại<br/>Làm nóng khuôn trước, chuẩn bị vật tư trước -25 phút"]
    C --> D["Bước 3: Tối ưu nội bộ<br/>Làm song song, kẹp nhanh -20 phút"]
    D --> E["Bước 4: Tiêu chuẩn hóa + huấn luyện<br/>-25 phút"]
    E --> F["Kết quả: 50 phút<br/>↓58%"]
    style F fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Máy ép nhựa đổi khuôn từ 120 phút xuống 50 phút, sản xuất lô nhỏ không còn "làm một lần cho xong", tồn kho WIP giảm 30%.

---

## XI. Nhóm an toàn & hoạt động cải tiến

### 37. Quy tắc Heinrich (an toàn)

**Một câu**: Cứ 1 vụ tai nạn nặng, phía sau khoảng 29 vụ nhẹ và 300 vụ suýt xảy ra — tiêu diệt các sự kiện "hú hồn" mới cắt đứt được chuỗi tai nạn.

```mermaid
flowchart TB
    A["300 sự kiện suýt xảy ra<br/>(suýt té / vi phạm bị phát hiện)"] --> B["29 vụ thương tích nhẹ<br/>(có ghi nhận)"]
    B --> C["1 vụ thương tích nặng hoặc tử vong"]
    D["Hành động quản lý:<br/>Sự kiện suýt xảy ra cũng phải báo cáo, phân tích, cải tiến<br/>(nhiều công ty đặt giải thưởng 'đề xuất hú hồn')"] -.-> A
    style C fill:#f8cecc,stroke:#b85450
    style D fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Một nhà máy thống kê 600 sự kiện suýt xảy ra (trượt chân / suýt kẹp tay) trong năm, 2 vụ thương tích. Cải tiến top 3 sự kiện suýt xảy ra (chống trượt sàn, lắp rào quang) năm sau về 0 vụ.

---

### 38. QCC - Vòng chất lượng

**Một câu**: Nhóm nhỏ nhân viên cùng khu vực làm việc tự nguyện thành lập vòng, dùng công cụ QC + PDCA để giải quyết vấn đề ngay bên cạnh mình.

```mermaid
flowchart LR
    Q1["1 Chọn đề tài<br/>(cấp trên định hướng + tự đề xuất)"] --> Q2["2 Nắm hiện trạng<br/>Phiếu kiểm tra + Phân tầng + Pareto"]
    Q2 --> Q3["3 Đặt mục tiêu<br/>(SMART)"]
    Q3 --> Q4["4 Phân tích<br/>Sơ đồ xương cá + 5Why"]
    Q4 --> Q5["5 Thực hiện đối sách<br/>(PDCA)"]
    Q5 --> Q6["6 Xác nhận hiệu quả<br/>So sánh trước / sau"]
    Q6 --> Q7["7 Tiêu chuẩn hóa<br/>Phòng ngừa tái phát"]
    Q7 --> Q8["8 Báo cáo và vấn đề còn lại"]
    style Q6 fill:#d5e8d4,stroke:#82b366
```

**Ví dụ (QCC "Giảm lỗi trượt vít ở chuyền lắp ráp")**: Hiện trạng 2.3% → vòng viên dùng phân tầng phát hiện vấn đề nằm ở mô-men xoắn tua vít điện → đối sách: tua vít lực cố định + kiểm tra điểm hàng ngày → sau 3 tháng giảm xuống 0.4%, tiết kiệm khoảng 180 triệu đồng chi phí tái làm mỗi năm.

---

### 39. Báo cáo A3

**Một câu**: Gói toàn bộ quá trình giải quyết vấn đề vào một tờ A3 — buộc bạn phải logic khép kín, kể lại gọn gàng trong một trang.

| Vùng trang | Nội dung | Điểm cần nhớ |
|---|---|---|
| Trên trái | Bối cảnh (tại sao làm) | Dùng dữ liệu nói điểm đau |
| Dưới trái | Hiện trạng và mục tiêu | Phân tầng + Pareto; mục tiêu SMART |
| Trên phải | Phân tích nguyên nhân gốc rễ | Sơ đồ xương cá + 5Why (đã kiểm chứng) |
| Giữa phải | Đối sách và kế hoạch | 5W2H rõ người chịu trách nhiệm |
| Dưới phải | Hiệu quả và tiêu chuẩn hóa | So sánh số liệu trước / sau; nhân rộng sang chuyền khác |

**Ví dụ**: A3 cải tiến tai nạn lao động — Bối cảnh (5 vụ/quý) → Hiện trạng (phân tầng: 60% là vận chuyển) → Nguyên nhân gốc rễ (5Why: đào tạo chỉ dừng ở ký nhận) → Đối sách (thi thực hành + xe đẩy trợ lực) → Hiệu quả (quý sau 0 vụ).

**Khi nào dùng**: Báo cáo vấn đề liên phòng ban, tổng kết QCC/8D, xin nguồn lực từ ban lãnh đạo.

---

## XII. Nhóm hiệu suất dây chuyền & logistics

### 40. Cân bằng dây chuyền (Line Balancing)

**Một câu**: Chênh lệch chu kỳ giữa các công đoạn càng nhỏ, hiệu suất dây chuyền càng cao — công đoạn nghẽn quyết định toàn bộ sản lượng.

```mermaid
flowchart LR
    A["Công đoạn 1<br/>20 giây"] --> B["Công đoạn 2<br/>35 giây ★nghẽn"]
    B --> C["Công đoạn 3<br/>25 giây"]
    C --> D["Công đoạn 4<br/>18 giây"]
    D --> E["Công đoạn 5<br/>22 giây"]
    F["Tỷ lệ cân bằng = Tổng thờ gian các công đoạn ÷ (Số công đoạn × Thờ gian nghẽn)<br/>= (20+35+25+18+22) ÷ (5×35) = 120÷175 ≈ 68.6%"]
    G["Cải tiến: tách / thêm người / song song tại công đoạn nghẽn<br/>Mục tiêu tỷ lệ cân bằng ≥ 85%"]
    B -.-> F
    F --> G
    style B fill:#f8cecc,stroke:#b85450
    style G fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Tách công đoạn 2 từ 35 giây thành hai người làm song song (18+17 giây), nghẽn mới trở thành 25 giây → tỷ lệ cân bằng = 120÷125 = **96%**, năng suất tăng 40% mà không cần mua thêm thiết bị.

---

### 41. Kanban

**Một câu**: Công đoạn sau cần bao nhiêu, công đoạn trước sản xuất bấy nhiêu — dùng thẻ thay lệnh sản xuất, loại bỏ sản xuất dư thừa.

```mermaid
flowchart LR
    A["Khách hàng / công đoạn sau"] -->|"Lấy hàng thì tháo thẻ"| B["Thùng thu thẻ"]
    B -->|"Thẻ = lệnh sản xuất"| C["Công đoạn trước chỉ sản xuất đúng số thẻ"]
    C -->|"Bổ sung"| D["Khu vực đệm siêu thị"]
    D --> A
    E["Công thức số thẻ<br/>= Nhu cầu trung bình × Chu kỳ bổ sung × (1 + Hệ số an toàn) ÷ Dung lượng thùng<br/>VD: 500 chiếc/ngày × 2 ngày × 1.2 ÷ 50 = 24 thẻ"]
    style E fill:#fff2cc,stroke:#d6b656
```

**Ví dụ**: Xưởng SMT dùng 2 thùng Kanban (một thùng đang dùng, một thùng đang bổ sung), chuyền không còn "núi bán thành phẩm", WIP giảm 60%.

---

### 42. VSM - Bản đồ dòng giá trị

**Một câu**: Vẽ "dòng thông tin + dòng vật liệu + thờ gian" trên một trang, nhìn thấy rõ lãng phí từ nguyên liệu đến xuất hàng.

```mermaid
flowchart LR
    S["Nhà cung cấp"] -->|"1 tuần 1 lần"| P1["Dập<br/>CT=10 giây<br/>Đổi khuôn 120 phút"]
    P1 -->|"Đẩy<br/>Lô 5000"| P2["Hàn<br/>CT=15 giây"]
    P2 -->|"Đẩy"| P3["Lắp ráp<br/>CT=45 giây"]
    P3 -->|"2 lần/ngày"| C["Khách hàng"]
    T["Tổng chu kỳ 23 ngày<br/>Thờ gian gia tăng giá trị chỉ 70 giây"]
    P1 -.-> T
    P2 -.-> T
    P3 -.-> T
    style T fill:#f8cecc,stroke:#b85450
```

**Cách dùng**: Vẽ bản đồ hiện trạng → đánh dấu tồn kho và chờ → vẽ bản đồ tương lai (dòng liên tục + kéo theo nhu cầu) → lập kế hoạch cải tiến. Trong ví dụ trên, trong 23 ngày chu kỳ chỉ có 70 giây thực sự gia công.

---

### 43. EOQ - Lô hàng kinh tế

**Một câu**: Đặt ít → chi phí đặt hàng cao; đặt nhiều → chi phí tồn kho cao; EOQ là điểm cân bằng tổng chi phí thấp nhất.

```mermaid
flowchart LR
    A["Nhu cầu năm D = 12000 chiếc"] --> B["Chi phí đặt hàng S = 500 ngàn đồng"]
    A --> C["Chi phí tồn kho H = 5000 đồng/chiếc/năm"]
    B --> D["EOQ = √(2DS ÷ H)"]
    C --> D
    D --> E["= √(2×12000×500÷5000)<br/>≈ 1549 chiếc/lần"]
    E --> F["Số lần đặt/năm = 12000÷1549 ≈ 8 lần<br/>Tổng chi phí tối thiểu ≈ 7.745 triệu đồng"]
    style E fill:#ffe6cc,stroke:#d79b00
```

**Điểm cần nhớ**: EOQ là mô hình lý tưởng, thực tế còn phải xem xét: MOQ, chiết khấu số lượng, diện tích kho, hạn sử dụng (đặc biệt thực phẩm/hóa chất).

---

## XIII. Nhóm quản lý hiện trường & thay đổi

### 44. Tam Hiện - Gemba Walk

**Một câu**: Hiện trường, hiện vật, hiện thực — đừng ngồi trong văn phòng xem báo cáo, hãy ra hiện trường xem vật thật, nắm thực trạng thực sự.

```mermaid
flowchart TB
    A["Vấn đề xảy ra"] --> B["Ra hiện trường<br/>Gemba"]
    B --> C["Xem hiện vật<br/>Sờ, đo, chụp ảnh"]
    C --> D["Nắm hiện thực<br/>Dùng dữ liệu kiểm chứng, không nghe báo cáo suông"]
    D --> E["Xử lý tại chỗ / mang nguyên nhân thật về"]
    F["Quản lý dành 30 phút/ngày đi tuần chuyền<br/>Ba câu hỏi: Tiêu chuẩn là gì? Thực tế ra sao? Tại sao có chênh lệch?"] -.-> B
    style E fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Báo cáo cho thấy tỷ lệ lỗi 0.5% bình thường, nhưng tổ trưởng tuần chuyền phát hiện công nhân bỏ qua công đoạn vệ sinh để chạy đua sản lượng — chỉ khi đứng tại hiện trường mới thấy được.

---

### 45. Quản lý thay đổi 4M

**Một câu**: Bất kỳ thay đổi nào về Người - Máy - Nguyên liệu - Phương pháp đều có thể mang rủi ro mới — thay đổi phải có quy trình, không được "đổi lén".

```mermaid
flowchart LR
    A["Đề xuất thay đổi<br/>4M: Người/Máy/Nguyên liệu/Phương pháp"] --> B["Đánh giá rủi ro<br/>Cập nhật FMEA"]
    B --> C["Chạy thử số lượng nhỏ<br/>Kiểm chứng CPK, GRR"]
    C --> D{"Khách hàng phê duyệt?<br/>Bắt buộc với chi tiết ô tô"}
    D -->|"Có"| E["Chuyển đổi chính thức<br/>Tăng cường kiểm tra lô đầu"]
    D -->|"Không"| F["Tiếp tục kiểm chứng hoặc từ bỏ"]
    E --> G["Cập nhật kế hoạch kiểm soát / SOP<br/>Thông báo các bên liên quan"]
    X["⚠ Thay đổi không được phê duyệt<br/>= Khiếu nại và sự cố hàng loạt"] -.-> A
    style X fill:#f8cecc,stroke:#b85450
    style G fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Đổi sang nhà cung cấp ốc vít mới (thay đổi Nguyên liệu) mà không kiểm chứng, dẫn đến cả lô 5000 sản phẩm mô-men xoắn không đạt bị thu hồi — quy trình thay đổi 4M chính là để ngăn chặn tai nạn như vậy.

---

### 46. Quản lý bằng mắt (Visual Management)

**Một câu**: Trạng thái hiện trường nhìn một cái là biết — bình thường hay bất thường không cần hỏi, dùng màu sắc, vạch kẻ, đèn tín hiệu để nói.

| Công cụ trực quan | Ví dụ |
|---|---|
| Quản lý màu sắc | Xanh = khu vực hàng đạt, đỏ = hàng lỗi, vàng = chờ kiểm tra |
| Vạch định vị | Bảng mẫu dụng cụ, vạch lối đi, vạch tồn kho tối đa (vượt là bất thường) |
| Andon | Dây kéo tại công đoạn, bất thường thì đèn sáng + chuông, tổ trưởng có mặt trong 3 phút |
| Bảng quản lý | Sản lượng / lỗi / trạng thái máy cập nhật hàng giờ |
| Đèn tín hiệu | Máy xanh = chạy / vàng = chờ / đỏ = hỏng |

**Tiêu chí đánh giá**: Một người lạ bước vào xưởng, có thể trong 30 giây nhận ra "chỗ nào bình thường, chỗ nào bất thường" không?

---

## XIV. Nhóm kiểm tra & hệ thống

### 47. AQL - Kiểm tra mẫu chấp nhận

**Một câu**: Không thể kiểm tra 100%, phải lấy mẫu theo thống kê — AQL cho bạn biết "lấy bao nhiêu, cho phép bao nhiêu lỗi".

```mermaid
flowchart LR
    A["Lô hàng N=1500 chiếc"] --> B["Tra bảng GB/T 2828.1<br/>Mức kiểm tra II thông thường"]
    B --> C["Cỡ mẫu n=125 chiếc"]
    C --> D["AQL=1.0<br/>Ac=3, Re=4"]
    D --> E{"Số lỗi trong 125 chiếc?"}
    E -->|"≤ 3"| F["Chấp nhận"]
    E -->|"≥ 4"| G["Từ chối<br/>Trả hàng / chọn lọc / nhận đặc biệt"]
    style F fill:#d5e8d4,stroke:#82b366
    style G fill:#f8cecc,stroke:#b85450
```

**Điểm cần nhớ**: AQL không phải "tỷ lệ lỗi cho phép", mà là tiêu chuẩn phán định mẫu; chi tiết an toàn quan trọng nên dùng SPC + kiểm tra 100% thay vì AQL. Mức kiểm tra I là nới lỏng (nhà cung cấp quen), III là siết chặt (nhà cung cấp mới / lô có vấn đề).

---

### 48. Kế hoạch kiểm soát (Control Plan)

**Một câu**: Ghi thành một trang "mỗi công đoạn kiểm soát gì, kiểm soát thế nào, lệch thì làm gì", là tài liệu cốt lõi của IATF.

**Ví dụ (trích kế hoạch kiểm soát công đoạn ép nhựa)**:

| Công đoạn | Đặc tính sản phẩm | Quy cách | Phương pháp đo | Tần suất | Phản ứng bất thường |
|---|---|---|---|---|---|
| Ép nhựa | Đường kính ngoài | φ10±0.05 | Thước kẹp | 5 chiếc/2 giờ | Dừng máy chỉnh khuôn + truy xuất |
| Ép nhựa | Thiếu liệu | Không cho phép | Mắt thường | 100% | Cách ly + chỉnh máy |
| Lắp ráp | Mô-men xoắn ốc | 1.2±0.1 N·m | Máy đo lực | 10 chiếc/ca | Dừng chuyền + siết lại |

**Điểm cần nhớ**: Kế hoạch kiểm soát liên kết với FMEA — những hạng mục RPN cao trong FMEA phải có biện pháp kiểm soát tương ứng trong kế hoạch kiểm soát.

---

### 49. SDCA - Vòng duy trì tiêu chuẩn

**Một câu**: PDCA làm mức độ vấn đề tăng lên, SDCA giữ thành quả không trượt ngược — tiêu chuẩn hóa trước, rồi mới tối ưu tiếp.

```mermaid
flowchart LR
    S["S Standardize<br/>Ghi đối sách vào SOP"] --> D["D Do<br/>Làm theo tiêu chuẩn mới"]
    D --> C["C Check<br/>Kiểm tra tỷ lệ tuân thủ"]
    C --> A["A Action<br/>Sửa lệch / đào tạo lại"]
    A -->|"Ổn định rồi"| S2["Chuyển sang vòng PDCA tiếp theo<br/>Thách thức mục tiêu cao hơn"]
    P["PDCA là leo thang<br/>SDCA là miếng đệm chống trượt"] -.-> S
    style S2 fill:#d5e8d4,stroke:#82b366
```

**Ví dụ**: Sau khi QCC giảm tỷ lệ lỗi từ 2.3% xuống 0.4%, nếu không ghi vào SOP và xác nhận hàng ngày, ba tháng sau rất có thể tăng lại 1.5% — đó là kết cục phổ biến khi thiếu SDCA.

---

### 50. FIFO - Vào trước ra trước & truy xuất

**Một câu**: Vật liệu xuất kho theo thứ tự nhập kho, thông tin lô hàng truy xuất được xuyên suốt — "cỗ máy thờ gian" của xử lý sự cố chất lượng.

```mermaid
flowchart LR
    A["Lô nguyên liệu nhập kho<br/>Nhãn: mã hàng + số lô + ngày"] --> B["Sắp xếp theo thứ tự nhập<br/>Vào trái ra phải / Vào trên ra dưới"]
    B --> C["Dùng trước hết lô nhập sớm nhất<br/>ERP bắt buộc FIFO"]
    C --> D["Ghi nhận số lô xuất hàng"]
    D --> E["Khi có khiếu nại: truy theo số lô<br/>Khóa hàng tồn kho / đang vận chuyển / tại khách hàng"]
    E --> F["Cách ly → xử lý → 8D"]
    style E fill:#ffe6cc,stroke:#d79b00
```

**Ví dụ**: Khách hàng phản ánh pin phồng, nhà máy khóa được lô hàng trong 30 phút là lô 12/3 dây chuyền B, cùng ngày thu hồi 200 chiếc đang vận chuyển và thông báo khách cách ly 1500 chiếc — không có hệ thống truy xuất, phản ứng như vậy là không thể.

---

## XV. Nhóm nhu cầu & chiến lược

### 51. Mô hình Kano

**Một câu**: Nhu cầu chia làm ba loại — yếu tố cơ bản thiếu là bị chửi, yếu tố hiệu suất càng tốt càng thích, yếu tố gây thích ngạc tạo ra truyền miệng.

```mermaid
flowchart TB
    K["Mô hình Kano"]
    K --> B["Cơ bản<br/>Thiếu thì phàn nàn, có thì im lặng<br/>VD: điện thoại gọi được"]
    K --> P["Hiệu suất<br/>Càng tốt càng hài lòng (tuyến tính)<br/>VD: pin 1 ngày → 3 ngày → 7 ngày"]
    K --> E["Gây thích ngạc<br/>Vượt mong đợi, tạo bất ngờ<br/>VD: giao hàng đúng giờ được bảo hiểm"]
    K --> I["Vô sai biệt<br/>Có hay không cũng không quan tâm"]
    style B fill:#f8cecc,stroke:#b85450
    style P fill:#ffe6cc,stroke:#d79b00
    style E fill:#d5e8d4,stroke:#82b366
```

**Ứng dụng**: Yếu tố cơ bản phải đạt 100%; yếu tố hiệu suất tối ưu theo tỷ lệ chi phí - lợi ích; yếu tố gây thích ngạc là vũ khí khác biệt hóa — và điều gây thích ngạc hôm nay sẽ trở thành kỳ vọng ngày mai.

---

### 52. PEST - Phân tích môi trường vĩ mô

**Một câu**: Trước khi vào thị trường / ngành mới, dùng bốn góc nhìn Chính trị, Kinh tế, Xã hội, Công nghệ để quét môi trường bên ngoài.

```mermaid
flowchart TB
    PEST["Phân tích PEST"]
    PEST --> P["P Chính trị / Pháp lý<br/>Ổn định chính sách, thuế quan, luật lao động<br/>VD: ưu đãi thuế đối với FDI tại Việt Nam"]
    PEST --> E["E Kinh tế<br/>Tỷ giá, chi phí nhân công, lạm phát<br/>VD: lương Việt Nam tăng 8-10%/năm"]
    PEST --> S["S Xã hội / Văn hóa<br/>Cơ cấu dân số, ngôn ngữ, tôn giáo<br/>VD: tuổi trung bình Việt Nam 32 tuổi"]
    PEST --> T["T Công nghệ<br/>Hạ tầng, mức độ tự động hóa, chuỗi cung ứng<br/>VD: ngành điện tử phía Bắc đã phát triển đầy đủ"]
    style PEST fill:#dae8fc,stroke:#6c8ebf
```

**Khi nào dùng**: Chọn địa điểm nhà máy ở nước ngoài (tình huống thường gặp với độc giả Việt - Trung), đánh giá khả thi kinh doanh mới, rút kinh nghiệm chiến lược hàng năm.

---

### 53. Ma trận Ansoff (chiến lược tăng trưởng)

**Một câu**: Dùng tổ hợp "Sản phẩm × Thị trường" mới/cũ tạo ra bốn hướng tăng trưởng, rủi ro từ thấp đến cao.

```mermaid
quadrantChart
    title Ma trận Ansoff - trục ngang: sản phẩm hiện tại → sản phẩm mới; trục dọc: thị trường hiện tại → thị trường mới
    x-axis "Sản phẩm hiện tại" --> "Sản phẩm mới"
    y-axis "Thị trường hiện tại" --> "Thị trường mới"
    quadrant-3 "Thâm nhập thị trường：bán thêm sản phẩm hiện cho khách hiện"
    quadrant-2 "Phát triển thị trường：sản phẩm hiện sang thị trường mới"
    quadrant-4 "Phát triển sản phẩm：sản phẩm mới cho khách hiện"
    quadrant-1 "Đa dạng hóa：sản phẩm mới + thị trường mới, rủi ro cao nhất"
```

**Ví dụ**: Lộ trình tăng trưởng của nhà máy snack — Thâm nhập thị trường (đưa sản phẩm hiện xuống siêu thị huyện) → Phát triển sản phẩm (ra phiên bản ít đường cho khách cũ) → Phát triển thị trường (xuất khẩu Đông Nam Á) → Đa dạng hóa (mua lại nhà máy nước giải khát).

---

## XVI. Nhóm lãnh đạo đội nhóm

### 54. RACI - Ma trận trách nhiệm

**Một câu**: Mỗi việc chỉ có một A (người chịu trách nhiệm giải trình), tránh "cả nhóm cùng quản = không ai quản" hoặc "đùn đẩy / tranh công".

| Nhiệm vụ | Quản lý dự án | Kỹ thuật | Chất lượng | Sản xuất |
|---|---|---|---|---|
| Nhập sản phẩm mới | **A** | R | C | C |
| Chạy thử | C | **A**/R | R | R |
| Thả hàng loạt | **A** | C | R | I |
| Xử lý khiếu nại | I | C | **A**/R | C |

R=Thực hiện Responsible, A=Chịu trách nhiệm giải trình Accountable, C=Tư vấn Consulted, I=Thông báo Informed. **Mỗi hàng phải có và chỉ có một A.**

---

### 55. GROW - Mô hình huấn luyện

**Một câu**: Huấn luyện cấp dưới không cần đưa đáp án, dùng bốn câu hỏi dẫn anh ta tự tìm ra — anh ta mới thực sự làm.

```mermaid
flowchart LR
    G["G Goal Mục tiêu<br/>Bạn muốn đạt gì?"] --> R["R Reality Hiện trạng<br/>Hiện tại tình hình thế nào?"]
    R --> O["O Options Phương án<br/>Có những cách nào có thể làm?"]
    O --> W["W Will Ý chí<br/>Bạn định làm gì? Bắt đầu khi nào?"]
    W --> F["Hành động do cấp dưới tự cam kết<br/>Tỷ lệ thực hiện cao hơn nhiều so với bị giao việc"]
    style F fill:#d5e8d4,stroke:#82b366
```

**Ví dụ đối thoại**: Quản đốc hỏi "Tháng này con muốn cải thiện gì?" (G) → "Hiện tại đổi khuôn mất bao lâu?" (R) → "Theo con thì rút ngắn bằng cách nào?" (O) → "Vậy tuần sau mình thử tách nội ngoại trước nhé?" (W) — SMED là do cấp dưới "tự chọn", triển khai không gặp kháng cự.

---

### 56. KPT - Rút kinh nghiệm nhẹ

**Một câu**: Keep tiếp tục giữ, Problem vấn đề, Try thử nghiệm tiếp theo — phương pháp rút kinh nghiệm nhẹ nhàng nhất.

```mermaid
flowchart LR
    K["K Keep Giữ lại<br/>Cái làm tốt, cố định thành thói quen"] --> P["P Problem Vấn đề<br/>Chỗ nào kẹt? Nguyên nhân gốc rễ là gì?"]
    P --> T["T Try Thử<br/>Lần sau thử đối sách nào?"]
    T --> K
    style T fill:#ffe6cc,stroke:#d79b00
```

**Ví dụ (phiên bản họp daily 3 phút)**: K=Hôm nay đổi khuôn nhanh hơn mục tiêu; P=Nhầm mã nguyên liệu mất 20 phút tìm; T=Ngày mai thử chia khu vực theo màu. **Nhẹ hơn GRAI, phù hợp chu kỳ ngắn (ngày/tuần).**

---

### 57. Năm chiến lược xử lý xung đột (TKI)

**Một câu**: Xung đột không đáng sợ, đáng sợ là chọn sai chiến lược — hai chiều "Kiên trì với mục tiêu" và "Hợp tác với quan hệ" quyết định cách chơi.

| Chiến lược | Kiên trì × Hợp tác | Tình huống phù hợp | Ví dụ |
|---|---|---|---|
| Cạnh tranh | Kiên trì cao, hợp tác thấp | Khẩn cấp + vấn đề nguyên tắc | Vấn đề an toàn phải dừng máy ngay lập tức |
| Hợp tác | Cả hai cao | Quan trọng và cần đôi bên cùng thắng | Cùng nhà cung cấp then chốt xây dựng tiêu chuẩn chất lượng |
| Thỏa hiệp | Trung bình cả hai | Thờ gian gấp, mỗi bên nhượng một bước | Tranh cãi ngày giao hàng, hai bên cùng lùi 2 ngày |
| Tránh né | Cả hai thấp | Chuyện nhỏ hoặc đang nóng giận | Cho cả hai bên nguôi 24 giờ rồi nói lại |
| Nhượng bộ | Kiên trì thấp, hợp tác cao | Duy trì quan hệ quan trọng hơn | Nhượng lộ trình kỹ thuật cho chuyên gia kỳ cựu |

**Sai lầm phổ biến**: Coi "tránh né" là yếu đuối — thực ra tạm dừng khi cảm xúc dâng trào chính là chuyên nghiệp.

---

### 58. Tháp nhu cầu Maslow (động viên)

**Một câu**: Nhu cầu của nhân viên từ sinh tồn đến tự thể hiện từng bậc thang — công nhân cần tiền, trụ cột cần phát triển, dùng sai động lực là tốn tiền vô ích.

```mermaid
flowchart TB
    M5["Tự thể hiện<br/>Dự án thử thách, đứng tên sáng chế, khởi nghiệp nội bộ"] --> M4["Được tôn trọng<br/>Chức danh, khen thưởng, phòng làm việc riêng"]
    M4 --> M3["Xã hội<br/>Team building, đôi buddy, câu lạc bộ"]
    M3 --> M2["An toàn<br/>Bảo hiểm, đơn hàng ổn định, đồ bảo hộ"]
    M2 --> M1["Sinh lý<br/>Lương, căn tin, ký túc, xe đưa đón"]
    style M1 fill:#f8cecc,stroke:#b85450
    style M5 fill:#d5e8d4,stroke:#82b366
```

**Ứng dụng trong nhà máy**: Động viên công nhân cơ bản tập trung M1-M2 (tăng ca minh bạch, cải thiện khu ở); tổ trưởng/kỹ sư thêm M3-M4 (chứng chỉ kỹ năng, giải thưởng nhân viên xuất sắc); với nhân tài cần M5, giao quyền chủ trì dự án cải tiến thường giữ chân tốt hơn tăng lương.

---

## XVII. Nhóm dự án & rủi ro

### 59. Đường găng - CPM (Critical Path Method)

**Một câu**: Con đường dài nhất trong dự án quyết định tổng thờ gian — nén những việc không nằm trên đường găng là làm vô ích.

```mermaid
flowchart LR
    A["A Thiết kế<br/>3 ngày"] --> B["B Mua hàng<br/>5 ngày"]
    A --> C["C Làm mẫu<br/>2 ngày"]
    B --> D["D Lắp ráp<br/>4 ngày"]
    C --> D
    D --> E["Bàn giao"]
    P["Đường găng A→B→D = 12 ngày<br/>Nén thờ gian chỉ có thể tác động ba hạng mục này<br/>C có 3 ngày dự phòng, không cần vội"] -.-> B
    style B fill:#ffe6cc,stroke:#d79b00
    style P fill:#fff2cc,stroke:#d6b656
```

**Ví dụ**: Cần rút ngắn 2 ngày, trả tiền cho nhà cung cấp ưu tiên (B) là hiệu quả; giục làm mẫu (C) hoàn toàn vô dụng — vì nó vốn đang chờ đợi.

---

### 60. Ma trận rủi ro (Xác suất × Tác động)

**Một câu**: Rủi ro nhiều không quản hết? Sắp xếp theo "Xác suất × Mức độ tác động", vùng đỏ xử lý trước.

```mermaid
flowchart TB
    M["Ma trận rủi ro RPN = P × I"]
    M --> H["Vùng đỏ P×I ≥ 12<br/>Hành động ngay: tránh/chuyển/giảm thiểu"]
    M --> MID["Vùng vàng 6 ~ 11<br/>Lập phương án dự phòng, kiểm tra định kỳ"]
    M --> L["Vùng xanh ≤ 5<br/>Chấp nhận, tiếp tục theo dõi"]
    E1["VD rủi ro cao: nhà cung cấp độc quyền đứt nguồn<br/>P=3 × I=5 = 15 → hai nguồn + tồn kho an toàn"] --> H
    E2["VD rủi ro trung bình: công nhân mới chưa thành thạo<br/>P=4 × I=2 = 8 → đôi buddy + tháng đầu có người hỗ trợ"] --> MID
    E3["VD rủi ro thấp: chuyển văn phòng<br/>P=2 × I=2 = 4 → đóng gói trước"] --> L
    style H fill:#f8cecc,stroke:#b85450
    style MID fill:#ffe6cc,stroke:#d6b656
    style L fill:#d5e8d4,stroke:#82b366
```

**Khi nào dùng**: Họp khởi động dự án, nhập sản phẩm mới, chuyển nhà máy, đánh giá rủi ro hàng năm. **Tổng quát hơn FMEA** (không giới hạn sản phẩm / quy trình).

---

## Tài nguyên mã nguồn mở có sẵn

| Tài nguyên | Mô tả |
|---|---|
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | Công cụ vẽ sơ đồ mã nguồn mở dùng cho toàn bộ file này |
| [MackDing/mentalModelMap](https://github.com/MackDing/mentalModelMap) | 79 sơ đồ tư duy kinh điển trực quan hóa (tiếng Trung, mã nguồn mở) |
| [《12 个人生工具》PDF](http://chenweixiang.github.io/docs/12_tools_for_everyone.pdf) | Tuyển tập sơ đồ SWOT/PDCA/6W2H/SMART/WBS/quy tắc 80/20 |
| [drawio (diagrams.net)](https://app.diagrams.net) | Công cụ vẽ miễn phí mã nguồn mở, có thư viện mẫu biểu đồ quản trị |
| [Excalidraw](https://excalidraw.com) | Bảng trắng phong cách vẽ tay mã nguồn mở, phù hợp phác thảo nhanh |
| [Miro Templates](https://miro.com/templates) | Thư viện mẫu SWOT/sơ đồ xương cá/5Why phong phú (một phần miễn phí) |
| [5xWhys Free Tools](https://5xwhys.com/tools/) | Tạo 5Why / sơ đồ xương cá / Pareto trực tuyến, có thể xuất file |

## Khuyến nghị sử dụng

1. **Trước tiên xem lộ trình**: chọn công cụ theo loại công việc hiện tại, không cần dùng cả 39.
2. **Kết hợp sử dụng**: 5W2H mô tả vấn đề (D2 của 8D) → sơ đồ xương cá phát tán → 5Why thu hẹp nguyên nhân gốc rễ → PDCA theo dõi cải tiến.
3. **Chỉnh sửa sơ đồ**: trực tiếp sửa chữ trong khối code `mermaid`, sau khi lưu GitHub / Typora / `index.html` sẽ tự động cập nhật.
