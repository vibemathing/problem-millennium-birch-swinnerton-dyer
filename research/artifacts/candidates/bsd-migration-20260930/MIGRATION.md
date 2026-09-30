# Pending migration proposal

Base: 5506238ec3e113c851f4f5d0a0cbc02ea6b1de95. All IDs here are proposed, not admitted.

The canonical contract and Harness remain unchanged. The source-enriched contract proposal targets the current upstream template schema, which is newer than this repository's frozen schema. Its source-list consolidation and changed contract digest require owner/importer review. Attempt and graph proposals intentionally bind the existing contract digest ab4afa6a9024ab0187168c78b1c71a0fdca2525c1528d403b332186e2c98d9f9, not the proposed digest fc144cfc0d06c88f649baeb21f81f21c7200c6c82a65338c4f0749e36a004f8a. If the contract changes, rebase all proposal bindings atomically through the trusted path before admission.

No independent verification receipt is supplied. Research drafts preserve the exact scoped result and open root bridge. The leaf is deliberately not a sufficient dependency for root closure. The richer six-way exploration is in RESEARCH.zh.md.

Reasoning checks: scope and assumptions explicit; dependency chain and witness explicit; exact negative controls included; symmetry (RH) and valuation invariant (BSD) examined; bounded loops terminate at 88 or six points; probability/extremal method not applicable to these exact deterministic checks; finite-to-global transition explicitly prohibited.

Expected compatibility boundary: pending inbox validation supports admission_request; strict diff validation still requires pre-admitted Attempt/Graph. Do not weaken this gate or manufacture truth-ledger entries to make CI green. A Harness maintainer must reconcile the gate separately, or a trusted importer must admit reviewed objects. Full root problem remains open in this submission.

Best local result: scoped prior exploratory draft and exact regression. Next obligation: source/statement review plus trusted admission; then the open bridge or next leaf described in the draft.
