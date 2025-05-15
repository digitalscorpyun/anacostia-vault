// update_last_updated.js — v1.0.0
module.exports = async (tp) => {
  const now = tp.date.now("YYYY-MM-DD HH:mm");
  await tp.frontmatter.set("last-updated", now);
};
