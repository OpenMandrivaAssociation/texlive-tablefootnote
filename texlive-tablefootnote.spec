# revision 27256
# category Package
# catalog-ctan /macros/latex/contrib/tablefootnote
# catalog-date 2012-07-30 11:22:32 +0200
# catalog-license lppl1.3
# catalog-version 1.0h
Name:		texlive-tablefootnote
Version:	1.0h
Release:	5
Summary:	Permit footnotes in tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tablefootnote
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tablefootnote.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the command \tablefootnote to be used in a
table or sidewaystableenvironment, where \footnote will not
work (and when using \footnotemark and \footnotetext, and
adjusting the counter as necessary, is too much work.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tablefootnote/tablefootnote.sty
%doc %{_texmfdistdir}/doc/latex/tablefootnote/README
%doc %{_texmfdistdir}/doc/latex/tablefootnote/tablefootnote-example.pdf
%doc %{_texmfdistdir}/doc/latex/tablefootnote/tablefootnote-example.tex
%doc %{_texmfdistdir}/doc/latex/tablefootnote/tablefootnote.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tablefootnote/tablefootnote.drv
%doc %{_texmfdistdir}/source/latex/tablefootnote/tablefootnote.dtx
%doc %{_texmfdistdir}/source/latex/tablefootnote/tablefootnote.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0h-1
+ Revision: 812888
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0g-1
+ Revision: 762727
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0e-2
+ Revision: 756430
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0e-1
+ Revision: 739921
- texlive-tablefootnote

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-1
+ Revision: 729698
- texlive-tablefootnote
- texlive-tablefootnote

